import datetime
import pytz

def time_in_range(interval):
    """Return true if the interval include actual time"""
    [start, end] = string_interval_to_time(interval)
    tz = pytz.timezone('Europe/Rome')
    now = datetime.datetime.now(tz).time()
    return (start <= now <= end)

def before_now(interval):
    """Return true if the interval is ended before actual time"""
    [start, end] = string_interval_to_time(interval)
    tz = pytz.timezone('Europe/Rome')
    now = datetime.datetime.now(tz).time()
    return now > end

def string_interval_to_time(interval):
    """Return 2 time retrieved from the string interval"""
    [timeStart, timeEnd] = interval.split('-')
    [startHour, startMin] = timeStart.split(':')
    [endHour, endMin] = timeEnd.split(':')
    start = datetime.time(int(startHour), int(startMin), 0)
    end = datetime.time(int(endHour), int(endMin), 0)
    return [start, end]