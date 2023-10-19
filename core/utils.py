from datetime import datetime


def is_valid_day_month(day: int, month: int) -> bool:
    """Utility for checking valid day and month
    :param day: a day number
    :param month: a month number
    :return: Provided day/month is valid
    """
    try:
        datetime(year=2, month=month, day=day)
    except Exception:
        return False
    return True
