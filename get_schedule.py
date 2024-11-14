import json
import os
from datetime import datetime
from typing import Optional


def get_schedule_from_json(identifier: str, date: str) -> Optional[dict]:
    filename = f"schedules/{identifier}.json"
    if not os.path.exists(filename):
        return None
    with open(filename, 'r') as file:
        schedule = json.load(file)
    date_obj = datetime.strptime(date, "%d.%m.%Y")
    day_of_week = date_obj.strftime("%A").lower()
    return schedule[day_of_week]