# This file is part of TorreArchimedeBot.
#
# TorreArchimedeBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TorreArchimedeBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TorreArchimedeBot.  If not, see <http://www.gnu.org/licenses/>.

import datetime
import pytz
import re
from datetime import time


def actual_time():
    tz = pytz.timezone('Europe/Rome')
    return datetime.datetime.now(tz).time()


def time_in_range(interval='12:00-12:00', time_to_check=actual_time()):
    """Return true if the interval include actual time"""
    [start, end] = string_interval_to_time(interval)
    return (start <= time_to_check <= end)


def before_now(interval):
    """Return true if the interval is ended before actual time"""
    [start, end] = string_interval_to_time(interval)
    return actual_time() > end


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


def parse_freefrom_time(string_time):
    lst = re.findall(r"[\w']+", string_time)
    if not lst:
        return "Time not valid"
    hour = lst[0]
    minutes = lst[1] if len(lst) > 1 else "00"
    if len(hour) >= 4:
        tmp = hour
        hour = tmp[0:2]
        minutes = tmp[2:4]

    try:
        hour = int(hour)
        minutes = int(minutes)
    except Exception:
        return "Time not valid"
    print(str(hour) + ":" + str(minutes))
    if not (0 <= hour <= 23 and 0 <= minutes <= 59):
        return "Time not valid"
    hour_min = time(hour, minutes)
    return hour_min
