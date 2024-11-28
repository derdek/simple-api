import json
import os
from typing import Optional


def get_exams_from_json(identifier: str, date: str) -> Optional[dict]:
    filename = f"exams/{identifier}.json"
    if not os.path.exists(filename):
        return None
    with open(filename, 'r') as file:
        exams = json.load(file)
    return exams.get(date)
