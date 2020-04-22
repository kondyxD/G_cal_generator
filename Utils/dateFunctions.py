import datefinder
import datetime
from datetime import datetime
import time


def getDateFromString(date_string):
    matches = list(datefinder.find_dates(date_string))
    if len(matches) > 0:
        return matches[0].utcnow().isoformat() + 'Z'
    else:
        return None


def getDateInterval(start_date_str='now', duration=1, unit='days'):
    units = ['hours', 'days', 'weeks']

    if unit in units:
        kwargs = {unit: duration}
    else:
        kwargs = {'days': duration}

    if start_date_str == 'now':
        return {'start_time': getISONowUTC(), 'end_time': dateToIso((getNow() + datetime.timedelta(**kwargs)))}

    matches = list(datefinder.find_dates(start_date_str))
    if len(matches):
        start_time = matches[0]
        end_time = start_time + datetime.timedelta(**kwargs)

    return {'start_time': dateToIso(start_time), 'end_time': dateToIso(end_time)}


def dateToIso(date_time):
    return date_time.isoformat() + 'Z'  # 'Z' indicates UTC time


def getISONowUTC():
    return dateToIso(datetime.datetime)


def getNow():
    return datetime.datetime.now()


def getSystemTimeZone():
    return 'Europe/Prague'


def formatDate(date):
    date = datetime.strptime(getDateFromString(date), '%c %Z%z')
    date = date.strftime("%A %d")
    return date
