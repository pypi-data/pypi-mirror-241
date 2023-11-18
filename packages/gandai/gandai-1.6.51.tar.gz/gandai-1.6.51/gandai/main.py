import re
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, dataclass, field

import requests
from bs4 import BeautifulSoup
from dacite import from_dict

import gandai as ts


def enrich_with_gpt(company: ts.models.Company) -> None:
    # return None
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
        "Accept": "text/html",
        "Referer": "https://www.google.com",
    }

    # company = ts.query.find_company_by_domain(domain)
    # print(domain)
    domain = company.domain
    try:
        resp = requests.get(f"http://www.{domain}", headers=HEADERS)
    except:
        print(f"failed on www.{domain}\ntrying without www")
        resp = requests.get(f"http://{domain}", headers=HEADERS)

    soup = BeautifulSoup(resp.text, "html.parser")
    homepage_text = soup.text.strip()
    homepage_text = re.sub(r"\s+", " ", homepage_text)
    print(homepage_text)

    messages = [
        {
            "role": "system",
            "content": f"You will help us evaluate {company.name} for acquisition.",
        },
        {
            "role": "system",
            "content": f"You will consider this existing information: {asdict(company)}",
        },
        {
            "role": "system",
            "content": f"You will consider this copy from the company homepage as the most up to date. homepage_text: {homepage_text}",
        },
        {
            "role": "system",
            "content": f"You will respond with only the JSON object.",
        },
        {
            "role": "system",
            "content": f"You are to create a asdict(Review) {ts.gpt.HOW_TO_REVIEW}",
        },
    ]

    # resp = ts.gpt.ask_gpt4(messages)
    resp = ts.gpt.ask_gpt35(messages)
    print(resp)
    review = from_dict(data_class=ts.models.Review, data=resp)
    print(review)
    company.meta = {**company.meta, **asdict(review)}
    ts.query.update_company(company)


def enrich_with_grata(company: str) -> None:
    resp = ts.grata.enrich(company.domain)
    company.name = company.name or resp.get("name")
    company.description = resp.get("description")
    company.meta = {**company.meta, **resp}
    ts.query.update_company(company)


def run_enrichment(domain: str) -> None:
    company = ts.query.find_company_by_domain(domain)
    if "company_uid" not in company.meta.keys():
        enrich_with_grata(company)
    if (
        company.meta.get("products", "") == ""
        and company.meta.get("services", "") == ""
    ):
        # if "was_acquired" not in company.meta.keys():
        # this means it will be running every time...
        enrich_with_gpt(company)


def run_similarity_search(search: ts.models.Search, domain: str) -> None:
    # dealcloud_companies =
    grata_companies = ts.grata.find_similar(domain=domain, search=search)
    ts.query.insert_companies_as_targets(
        companies=grata_companies, search_uid=search.uid, actor_key="grata"
    )


def run_criteria_search(search: ts.models.Search) -> None:
    # don't have to pass the event because the criteria
    # is the event that we're responding to
    grata_companies = ts.grata.find_by_criteria(search)
    ts.query.insert_companies_as_targets(
        companies=grata_companies, search_uid=search.uid, actor_key="grata"
    )


def run_maps_search(search: ts.models.Search, event: ts.models.Event) -> None:
    existing_search_domains = ts.query.unique_domains(search_uid=search.uid)[
        "domain"
    ].to_list()

    def build_place(place_id: str, search: ts.models.Search) -> None:
        resp = ts.google.gmaps.place(
            place_id=place_id, fields=["name", "website", "reviews"]
        )
        place = resp["result"]  # these reviews are valueable
        domain = ts.helpers.clean_domain(place.get("website"))
        if domain is None:
            return None
        if domain in existing_search_domains:
            print(f"domain {domain} already in search. skipping...")
            return None
        new_company = ts.models.Company(
            name=place["name"],
            domain=domain,
        )
        ts.query.insert_company(new_company)
        company = ts.query.find_company_by_domain(new_company.domain)

        event = ts.models.Event(
            search_uid=search.uid,
            type="create",
            domain=company.domain,
            actor_key="google",
            data={
                "place": place,  # could limit some
            },
        )

        ts.query.insert_event(event)

    q = event.data["query"]
    results = ts.google.get_google_places(q=q)
    print(results)
    # with ThreadPoolExecutor(max_workers=10) as executor:
    #     executor.map(build_place, results['place_id'].tolist())
    for place in results["place_id"].tolist():
        build_place(place_id=place, search=search)


def run_google_search(search: ts.models.Search, event: ts.models.Event) -> None:
    q = event.data["q"]
    assert len(q) > 0, "q must be a non-empty string"
    results = ts.google.search(q=q, count=event.data.get("count", 10))
    results["domain"] = results["link"].apply(lambda x: ts.helpers.clean_domain(x))
    results = results.rename(columns={"snippet": "description"})
    print(results)
    ts.query.insert_companies_as_targets(
        companies=results[["domain", "description"]].to_dict(orient="records"),
        search_uid=event.search_uid,
        actor_key=event.actor_key,
    )


def handle_prompt(event: ts.models.Event) -> None:
    messages = [
        {
            "role": "system",
            "content": ts.gpt.HOW_TO_RESPOND,
        },
        {
            "role": "system",
            "content": ts.gpt.HOW_TO_IMPORT,
        },
        {
            "role": "system",
            "content": ts.gpt.HOW_TO_TRANSITION,
        },
        {
            "role": "system",
            "content": ts.gpt.HOW_TO_GOOGLE,
        },
        {
            "role": "system",
            "content": ts.gpt.HOW_TO_GOOGLE_MAPS,
        },
        {
            "role": "system",
            "content": f"the search_uid is {event.search_uid}",
        },
        {
            "role": "system",
            "content": f"the actor_key is {event.actor_key}",
        },
        {"role": "user", "content": event.data["prompt"]},
    ]
    resp = ts.gpt.ask_gpt4(messages)
    # resp = ts.gpt.ask_gpt35(messages) # can be so much faster
    print(resp)
    for event in resp["events"]:
        e = from_dict(ts.models.Event, event)
        ts.query.insert_event(e)


def process_event(event_id: int) -> None:
    print("processing event...")
    event: ts.models.Event = ts.query.find_event_by_id(event_id)
    print(event)
    search = ts.query.find_search(uid=event.search_uid)
    domain = event.domain
    if event.type == "create":
        run_enrichment(domain=domain)  # lets unleash the beast
    elif event.type == "advance":
        run_enrichment(domain=domain)
    elif event.type == "validate":
        run_enrichment(domain=domain)
        run_similarity_search(search=search, domain=domain)
    elif event.type == "send":
        run_enrichment(domain=domain)
    elif event.type == "client_approve":
        run_enrichment(domain=domain)
        run_similarity_search(search=search, domain=domain)  # n=
    elif event.type == "reject":
        pass
    elif event.type == "client_reject":
        pass
    elif event.type == "conflict":
        run_enrichment(domain=domain)
        run_similarity_search(search=search, domain=domain)
    elif event.type == "client_conflict":
        # run_enrichment(domain=domain)
        # run_similarity_search(search=search, domain=domain)
        pass

    ## actions
    elif event.type == "prompt":
        handle_prompt(event=event)
    elif event.type == "criteria":
        if len(event.data["inclusion"]["keywords"]) > 0:
            run_criteria_search(search=search)
    elif event.type == "maps":
        run_maps_search(search=search, event=event)
    elif event.type == "google":
        run_google_search(search=search, event=event)
    elif event.type == "import":
        data = event.data
        ts.query.insert_targets_from_domains(
            domains=data["domains"],
            search_uid=event.search_uid,
            actor_key=event.actor_key,
            stage=data.get("stage", "advance"),
        )

    elif event.type == "reset":
        print("💣 Resetting Inbox...")
        ts.query.reset_inbox(search_uid=search.uid)

    elif event.type == "update":
        if domain:
            company = ts.query.find_company_by_domain(domain)
            if event.data.get("name"):
                company.name = event.data["name"]
            if event.data.get("description"):
                description = event.data["description"]
                if description.startswith("/gpt"):
                    company.description = gpt.get_company_summary(domain=domain)
                else:
                    company.description = event.data["description"]

            company.meta = {**company.meta, **event.data}
            ts.query.update_company(company)
        else:
            search.meta = {**search.meta, **event.data}
            ts.query.update_search(search)

    elif event.type == "transition":
        # do we want this?
        for domain in event.data["domains"]:
            ts.query.insert_event(
                ts.models.Event(
                    search_uid=search.uid,
                    domain=domain,
                    type=event.data["type"],
                    actor_key=event.actor_key,
                )
            )
