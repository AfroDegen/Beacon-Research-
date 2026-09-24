# search.py

from serpapi import GoogleSearch
from urllib.parse import urlparse
from config import SERPAPI_KEY


def extract_domain(url):
    return urlparse(url).netloc.replace("www.", "")


def get_google_domains(query):

    params = {
        "q": query,
        "num": 10,
        "api_key": SERPAPI_KEY
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    domains = []

    for result in results.get("organic_results", []):
        link = result.get("link")

        if link:
            domains.append(
                extract_domain(link)
            )

    return domains
