from datetime import datetime, timedelta


def utc_current_time_formatted():
    current_time = datetime.utcnow()
    format_str = "%d/%m/%Y %H:%M:%S"
    formatted_time = current_time.strftime(format_str)
    return formatted_time


def add_minutes_to_utc_time(minutes: int, time=None):
    if time is None:
        time = utc_current_time_formatted()

    # Convert a string to a datetime object
    time = datetime.strptime(time, "%d/%m/%Y %H:%M:%S")

    new_time = time + timedelta(minutes=minutes)
    format_str = "%d/%m/%Y %H:%M:%S"
    formatted_time = new_time.strftime(format_str)
    return formatted_time
