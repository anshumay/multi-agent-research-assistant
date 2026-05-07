import json
import re


def clean_json_response(text):
    """
    Removes markdown wrappers like ```json ... ```
    """

    text = re.sub(r"```json", "", text)
    text = re.sub(r"```", "", text)

    return text.strip()


def parse_json(output):
    try:
        cleaned_output = clean_json_response(output)

        return json.loads(cleaned_output)

    except Exception as e:
        print("\n⚠️ JSON parsing failed")
        print(e)

        return {
            "error": "Parsing failed",
            "raw_output": output
        }