from datetime import datetime
import const.tg as tg

def formate_date(date_string):
    from_date = datetime.fromtimestamp(date_string)
    delta = datetime.now() - from_date
    years = int(delta.days / 365.25)
    months = int(delta.days / 30)
    if years > 0:
        return '{y} year{s}'.format(y=years, s=('s' if years > 1 else ''))
    if months > 0:
        return '{y} month{s}'.format(y=months, s=('s' if months > 1 else ''))
    if delta.days > 0:
        return '{d} day{s}'.format(d=delta.days, s=('s' if delta.days > 1 else ''))
    return from_date.strftime('%H:%M')

def format_status(status):
    result = 'unknown'
    try:
        if status[tg.offline]:
            return tg.offline
    except Exception:
        result = result
    try:
        if status[tg.online]:
            return tg.online
    except Exception:
        result = result
    try:
        if status[tg.recently]:
            return tg.recently
    except Exception:
        result = result
    return result
