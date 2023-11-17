from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field, asdict
from time import time


import pandas as pd
from dacite import from_dict

import gandai as ts
from gandai import query, models, gpt
from gandai.sources import GrataWrapper as grata
# from gandai.sources import GoogleMapsWrapper as google
import googlemaps
gmaps = googlemaps.Client(key=ts.secrets.access_secret_version("GOOLE_MAPS_KEY"))

import requests
import re
from bs4 import BeautifulSoup
import json

HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
        "Accept": "text/html",
        "Referer": "https://www.google.com",
    }

@dataclass
class Review:
    domain: str  # the domain of the company
    products: str = field(default="")  # csv of the products offered by the company
    services: str = field(default="")  # csv of the services offered by the company

REVIEW = """
    @dataclass
    class Review:
        domain: str  # the domain of the company
        products: str = field(default="") # csv of the products offered by the company. products are physical goods sold by the company. do not list services here.
        services: str = field(default="") # csv of the services offered by the company. services are intangible goods offered by the company. do not list products here.
    """


def enrich_with_gpt(domain: str) -> None:
    # return None

    company = ts.query.find_company_by_domain(domain)
    print(domain)
    try:
        resp = requests.get(f"http://www.{domain}", headers=HEADERS)
    except:
        print(f"failed on www.{domain}\ntrying without www")
        resp = requests.get(f"http://{domain}", headers=HEADERS)

    soup = BeautifulSoup(resp.text, "html.parser")
    homepage_text = soup.text.strip()
    homepage_text = re.sub(r"\s+", " ", homepage_text)
    print(homepage_text)

    # homepage_links = soup.find_all("a")
    # homepage_links = [link.get("href") for link in homepage_links]
    # # ask which ones should I read?

    # HOW_TO_REVIEW = """    
    # Examples of products for this search:
    # A product is not a brand, do not list brands here
    # - HVAC: a system that heats and cools your house. 
    #     Consider all of these as grouped under HVAC Furnaces, Air Purifiers, Air Conditioners, Boilers, Ductless HVAC Systems are all HVAC
    # - Plumbing: moves water and waste into and out of your house
    #     Consider water heaters, sump pumps, clogged drains, water filtration systems, plumbing fixtures, pipes fittings as grouped under Plumbing
    # - Electrical: powers your house
    #     Consider generators as grouped under Electrical

    # Examples of services for this search:
    # - Repair: a repair is a one time service
    # - Maintenance: is an agreement to maintain a product over time
    # - Replacement: is what it sounds like - replacing a product
    # - Installation: is what it sounds like - installing a product

    # You will only select from these categories. If you are unsure, you can leave it blank.
    
    # """

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
            "content": f"You are to create a asdict(Review) {REVIEW}, fill it out and return it to me as valid JSON",
        },
        # {
        #     "role": "user",
        #     "content": HOW_TO_REVIEW,
        # },
    ]

    resp = ts.gpt.ask_gpt4(messages)
    print(resp)
    review = from_dict(data_class=Review, data=resp)
    print(review)
    company.meta = {**company.meta, **asdict(review)}
    ts.query.update_company(company)


def enrich_with_grata(company: str) -> None:
    resp = grata.enrich(company.domain)
    company.name = company.name or resp.get("name")
    company.description = resp.get("description")
    company.meta = {**company.meta, **resp}
    query.update_company(company)


def enrich_company(domain: str) -> None:
    company = query.find_company_by_domain(domain)
    if "company_uid" not in company.meta.keys():
        enrich_with_grata(company)
    if "was_acquired" not in company.meta.keys():
        enrich_with_gpt(domain)


def run_similarity_search(search: ts.models.Search, domain: str) -> None:
    # dealcloud_companies =
    grata_companies = grata.find_similar(domain=domain, search=search)
    query.insert_companies_as_targets(
        companies=grata_companies, search_uid=search.uid, actor_key="grata"
    )


def run_criteria_search(search: ts.models.Search) -> None:
    # don't have to pass the event because the criteria
    # is the event that we're responding to
    grata_companies = grata.find_by_criteria(search)
    query.insert_companies_as_targets(
        companies=grata_companies, search_uid=search.uid, actor_key="grata"
    )


def run_maps_search(search: ts.models.Search, event: ts.models.Event) -> None:
    
    def build_place(place_id: str, search: ts.models.Search) -> None:
        resp = gmaps.place(place_id=place_id, fields=["name", "website","reviews"])
        place = resp['result'] # these reviews are valueable

        domain = ts.helpers.clean_domain(place.get("website"))
        if domain is None:
            return None
        new_company = ts.models.Company(
            name=place["name"],
            domain=domain,
        )
        ts.query.insert_company(new_company)
        company = ts.query.find_company_by_domain(new_company.domain)

        # hits grata
        # resp = ts.grata.enrich(company.domain)
        # company.name = company.name or resp.get("name")
        # company.description = resp.get("description")
        # company.meta = {**company.meta, **resp}
        # ts.query.update_company(company)

        # hits website, updates w gpt
        # enrich_with_gpt(company.domain)

        # yeah I think we do want to create this target

        event = ts.models.Event(
            search_uid=search.uid,
            type="create",
            domain=company.domain,
            actor_key='google',
            data={
                "place": place, # could limit some 
            }
        )

        ts.query.insert_event(event)
    
    
    q = event.data["query"]
    results = ts.google.get_google_places(q=q)
    print(results)
    # with ThreadPoolExecutor(max_workers=10) as executor:
    #     executor.map(build_place, results['place_id'].tolist())
    for place in results['place_id'].tolist():
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
    ## will create new events
    # prompt = """
    # You will search Google for the following queries:
    # residential deck contractors austin tx

    # You will return 20 results for each query.
    # """
    prompt = event.data["prompt"]
    search_uid = event.search_uid
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
            "content": f"the search_uid is {search_uid}",
        },
        {
            "role": "system",
            "content": f"the actor_key is {event.actor_key}",
        },
        {"role": "user", "content": prompt},
    ]
    resp = ts.gpt.ask_gpt4(messages)
    # resp = ts.gpt.ask_gpt35(messages) # so much faster
    print(resp)
    for event in resp["events"]:
        e = from_dict(ts.models.Event, event)
        ts.query.insert_event(e)


def process_event(event_id: int) -> None:
    print("processing event...")

    event: models.Event = query.find_event_by_id(event_id)
    print(event)
    search = query.find_search(
        uid=event.search_uid
    )  # this would fail if insert search is an event
    domain = event.domain
    if event.type == "create":
        # enrich_company(domain=domain)  # lets unleash the beast
        # gpt enrich here
        pass
    elif event.type == "advance":
        enrich_company(domain=domain)
    elif event.type == "validate":
        enrich_company(domain=domain)
        run_similarity_search(search=search, domain=domain)

    elif event.type == "send":
        enrich_company(domain=domain)
    elif event.type == "client_approve":
        enrich_company(domain=domain)
        run_similarity_search(search=search, domain=domain)  # n=
    elif event.type == "reject":
        pass
    elif event.type == "client_reject":
        pass
    elif event.type == "conflict":
        enrich_company(domain=domain)
        run_similarity_search(search=search, domain=domain)
    elif event.type == "client_conflict":
        # enrich_company(domain=domain)
        # run_similarity_search(search=search, domain=domain)
        pass

    ## builders
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
        query.insert_targets_from_domains(
            domains=data["domains"],
            search_uid=event.search_uid,
            actor_key=event.actor_key,
            stage=data.get("stage", "advance"),
        )

    elif event.type == "reset":
        print("💣 Resetting Inbox...")
        query.reset_inbox(search_uid=search.uid)

    elif event.type == "update":
        if domain:
            company = query.find_company_by_domain(domain)
            if event.data.get("name"):
                company.name = event.data["name"]
            if event.data.get("description"):
                description = event.data["description"]
                if description.startswith("/gpt"):
                    company.description = gpt.get_company_summary(domain=domain)
                else:
                    company.description = event.data["description"]

            company.meta = {**company.meta, **event.data}
            query.update_company(company)
        else:
            search.meta = {**search.meta, **event.data}
            query.update_search(search)

    elif event.type == "transition":
        for domain in event.data["domains"]:
            query.insert_event(
                ts.models.Event(
                    search_uid=search.uid,
                    domain=domain,
                    type=event.data["type"],
                    actor_key=event.actor_key,
                )
            )
