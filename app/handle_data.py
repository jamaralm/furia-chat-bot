import json
from datetime import datetime

def load_data(file_url):
    try:
        with open(file_url, 'r', encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_data(data, file_url):
    try:
        with open(file_url, 'w') as file:
            json.dump(data, file, indent=2)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def remove_data(file_url, id):
    data = load_data(file_url)

    updated_data = [data_to_remove for data_to_remove in data if data_to_remove['id'] != id]

    save_data(updated_data, file_url)

def check_match_date(): 
    matches = load_data('app/data/matches.json')
    actual_time = datetime.now()

    for match in matches:
        match_datetime_str = f"{match['date']} {match['time']}"
        match_datetime = datetime.strptime(match_datetime_str, "%d/%m/%Y %H:%M")

        if match_datetime > actual_time:
            time_remaining = match_datetime - actual_time
            return time_remaining, match
        else:
            remove_data('app/data/matches.json', match['id'])
    return None, None