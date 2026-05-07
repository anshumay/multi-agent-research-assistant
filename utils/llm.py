from openai import OpenAI
from dotenv import load_dotenv
import os
import time

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def call_llm(prompt, temperature=0.3, retries=3):
    for attempt in range(retries):

        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature
            )

            return response.choices[0].message.content

        except Exception as e:
            print(f"\n⚠️ LLM call failed (Attempt {attempt+1})")
            print(e)

            time.sleep(2)

    return "LLM call failed after retries."