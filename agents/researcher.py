from tools.search import search_web
from utils.llm import call_llm

def research_agent(query):
    search_results = search_web(query)

    prompt = f"""
    You are a research agent.

    Use ONLY the provided search results.

    Return STRICT JSON:

    {{
      "facts": [
        {{
          "category": "definition / architecture / impact / history",
          "fact": "string",
          "source": "url"
        }}
      ]
    }}

    Rules:
    - No duplicate facts
    - Merge similar facts
    - Keep concise

    Search Results:
    {search_results}
    """

    return call_llm(prompt)