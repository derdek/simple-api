from datetime import datetime


def get_is_numerator(date_str: str) -> bool:
    start_date = datetime(2024, 9, 2)
    date_obj = datetime.strptime(date_str, "%d.%m.%Y")
    delta = date_obj - start_date
    days_since_start = delta.days
    weeks = days_since_start // 7
    return weeks % 2 == 0
