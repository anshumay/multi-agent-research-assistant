from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_llm(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response.choices[0].message.content


def writer_agent(analysis_data):
    prompt = f"""
    You are a professional report writer.

    Use the structured insights below to create a detailed report.

    Structure:
    - Title
    - Executive Summary
    - Key Insights
    - Detailed Analysis
    - Conclusion

    Analysis:
    {analysis_data}
    """

    return call_llm(prompt)