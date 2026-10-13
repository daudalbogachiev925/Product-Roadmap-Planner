import json
from datetime import datetime

def load(path="initiatives.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def save(data, path="initiatives.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def to_gantt(data):
    return [{
        "Task": i["name"],
        "Start": i["start"],
        "Finish": i["end"],
        "Owner": i.get("owner", ""),
        "Status": i.get("status", "planned"),
    } for i in data]
