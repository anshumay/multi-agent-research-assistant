from tools.search import search_web
from utils.llm import call_llm
from utils.memory import load_memory

def research_agent(query):
    search_results = search_web(query)

    memory = load_memory()

    recent_memory = memory[-3:]

    prompt = f"""
    You are a research agent.
    Use:
    - Current search results
    - Previous research memory

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

    Previous Research History:
    {recent_memory}

    Search Results:
    {search_results}

    

    """

    return call_llm(prompt)