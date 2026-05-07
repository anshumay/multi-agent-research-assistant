from utils.llm import call_llm

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