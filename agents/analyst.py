from openai import OpenAI
from dotenv import load_dotenv
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


def analyst_agent(research_data):
    prompt = f"""
    You are a data analyst.

    Analyze the structured research data.

    Return STRICT JSON:

    {{
      "insights": [
        {{
          "theme": "string",
          "insight": "string",
          "supporting_facts": []
        }}
      ]
    }}

    Research Data:
    {research_data}
    """

    return call_llm(prompt)