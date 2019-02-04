from datetime import datetime

def username(user=None, chat=None):
    if user or chat and chat['type'] == 'private':
        if not user:
            user = chat
        name = user['first_name']
        if user['last_name']:
            name += ' ' + user['last_name']
    elif chat:
        name = chat['title']
    return name if name else 'Unknown'

def time(date):
    from_date = datetime.fromtimestamp(date)
    delta = datetime.now() - from_date
    years = int(delta.days / 365.25)
    months = int(delta.days / 30)
    hours = delta.seconds//3600
    minutes = (delta.seconds//60)%60
    if years > 0:
        return '{y} year{s}'.format(y=years, s=('s' if years > 1 else ''))
    if months > 0:
        return '{y} month{s}'.format(y=months, s=('s' if months > 1 else ''))
    if delta.days > 0:
        return '{d} day{s}'.format(d=delta.days, s=('s' if delta.days > 1 else ''))
    if hours == 0 and minutes > 0:
        return '{d} min'.format(d=minutes)
    if delta.seconds < 5:
        return 'just now'
    if delta.seconds < 60:
        return '{d} sec'.format(d=delta.seconds)
    return from_date.strftime('%H:%M')

def date(date):
    from_date = datetime.fromtimestamp(date)
    now = datetime.now()
    days = now.day - from_date.day
    if now.year - from_date.year > 0:
        return from_date.strftime('%Y')
    if days >= 7:
        return from_date.strftime('%b')
    if days > 0 and days < 7:
        return from_date.strftime('%a')
    return from_date.strftime('%H:%M')
