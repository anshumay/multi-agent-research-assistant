import json

def parse_json(output):
    try:
        return json.loads(output)
    except Exception as e:
        print("⚠️ JSON parsing failed")
        print(e)
        return output