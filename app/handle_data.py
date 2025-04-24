import json

def load_data(file_url):
    try:
        with open(file_url, 'r', encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []