from serpapi import GoogleSearch
import os
from dotenv import load_dotenv
from utils.config import get_secret

load_dotenv()

def search_web(query):
    params = {
    "q": query,
    "api_key": get_secret("SERPAPI_API_KEY"),
    "num": 5
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    organic_results = results.get("organic_results", [])

    snippets = []

    for result in organic_results:
        title = result.get("title", "")
        snippet = result.get("snippet", "")
        link = result.get("link", "")

        snippets.append(
            f"Title: {title}\n"
            f"Snippet: {snippet}\n"
            f"Source: {link}\n"
        )

    return "\n".join(snippets)