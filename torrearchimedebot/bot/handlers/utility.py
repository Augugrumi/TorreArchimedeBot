import datetime
import pytz


def time_in_range(interval):
    """Return true if the interval include actual time"""
    [start, end] = string_interval_to_time(interval)
    return (start <= actual_time() <= end)


def before_now(interval):
    """Return true if the interval is ended before actual time"""
    [start, end] = string_interval_to_time(interval)
    return actual_time() > end


def actual_time():
    tz = pytz.timezone('Europe/Rome')
    return datetime.datetime.now(tz).time()


def string_interval_to_time(interval):
    """Return 2 time retrieved from the string interval"""
    [timeStart, timeEnd] = interval.split('-')
    [startHour, startMin] = timeStart.split(':')
    [endHour, endMin] = timeEnd.split(':')
    start = datetime.time(int(startHour), int(startMin), 0)
    end = datetime.time(int(endHour), int(endMin), 0)
    return [start, end]


def retrieve_rooms():
    rooms = [
        '1A150',
        '1AD100',
        '1BC45',
        '1BC50',
        '1C150',
        '1AD100',
        '2AB40',
        '2AB45',
        '2BC30',
        '2BC60',
        'LabTA',
        'LabP036',
        'LabP140',
        'LuF1',
        'LuM250',
        'P200'
    ]
    return rooms
