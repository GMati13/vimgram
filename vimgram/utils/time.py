from datetime import datetime, timedelta

def seconds_to_next_day():
    now = datetime.now()
    return (timedelta(hours=24) - timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)).seconds
