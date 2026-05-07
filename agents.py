from openai import OpenAI
import os
from dotenv import load_dotenv
from tools import search_web
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_llm(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content


# 1. Research Agent
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
    - No duplicates
    - Merge similar facts
    - Keep concise

    Search Results:
    {search_results}
    """

    return call_llm(prompt)


def parse_json(output):
    try:
        return json.loads(output)
    except:
        print("⚠️ JSON parsing failed, returning raw text")
        return output

# 2. Analyst Agent
def analyst_agent(research_data):
    prompt = f"""
    You are a data analyst.

    You are given structured research data.

    Input:
    {research_data}

    Return STRICT JSON:

    {{
      "insights": [
        {{
          "theme": "string",
          "insight": "string",
          "supporting_facts": ["fact1", "fact2"]
        }}
      ]
    }}

    Rules:
    - Group related facts
    - Remove redundancy
    - Focus on insights, not repetition
    """

    return call_llm(prompt)


# 3. Writer Agent
def writer_agent(analysis_data):
    prompt = f"""
    You are a professional report writer.

    Use the structured insights below to create a report.

    Input:
    {analysis_data}

    Structure:
    - Title
    - Executive Summary
    - Key Insights
    - Detailed Analysis
    - Conclusion

    Make it clear, concise, and professional.
    """

    return call_llm(prompt)