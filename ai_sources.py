import json

try:
    with open("ai_sources.json") as f:
        DATA = json.load(f)

except FileNotFoundError:
    DATA = {}

def get_ai_sources(query):
    return DATA.get(query, [])
