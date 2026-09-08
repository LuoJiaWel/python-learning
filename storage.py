import json

def load_records():
    try:
        with open("records.json", "r") as file:
            records = json.load(file)
        return records
    except FileNotFoundError:
        return []


def save_records(records):
    with open("records.json", "w") as file:
        json.dump(records, file)