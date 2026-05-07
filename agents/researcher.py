from openai import OpenAI
from dotenv import load_dotenv
from tools.search import search_web
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_llm(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content


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