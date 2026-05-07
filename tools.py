from serpapi import GoogleSearch
import os
from dotenv import load_dotenv

load_dotenv()

def search_web(query):
    params = {
        "q": query,
        "api_key": os.getenv("SERPAPI_API_KEY"),
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
        snippets.append(f"{title}\n{snippet}\n{link}\n")

    return "\n".join(snippets)