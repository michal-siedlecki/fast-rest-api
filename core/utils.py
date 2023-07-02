def is_valid_day_month(day, month):
    valid_month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return day <= valid_month_days[month - 1]
