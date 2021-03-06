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

import requests
import json
import html
import logging
import threading
import pytz

from lxml import html as htmllxml
from .utility import *
from datetime import time


class Results:
    def __init__(self, time='', activity='', professor='', activityType=''):
        if (time != ''):
            [timeStart, timeEnd] = time.split(' - ')
            self.timeStart = timeStart
            self.timeEnd = timeEnd
        else:
            self.timeStart = ''
            self.timeEnd = ''
        self.activity = activity
        self.professor = professor
        self.activityType = activityType

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def isEmpty(self):
        return (self.timeStart == '' and
                self.timeEnd == '' and
                self.activity == '' and
                self.professor == '' and
                self.activity == '')


def json2Schedule(jsonString):
    data = json.loads(jsonString)
    schedule = data["schedule"]
    results = []
    for r in schedule:
        key = r
        r = r.replace("-", " - ")
        results.append(
            Results(r, schedule[key][0], schedule[key][1], schedule[key][2]))
    return Schedule(data["room"], results)


class Schedule:
    def __init__(self, room, records):
        self.room = room
        self.schedule = {}
        for res in records:
            if (not res.isEmpty()):
                l = [None] * 3
                l[0] = res.activity
                l[1] = res.professor
                l[2] = res.activityType
                time = res.timeStart + "-" + res.timeEnd
                self.schedule[time] = l

    def getSchedule(self):
        return self.schedule

    def getRoom(self):
        return self.room

    def now(self):
        toReturn = ''
        t = ''
        for time in self.schedule:
            if (time_in_range(time)):
                toReturn = self.schedule[time]
                t = time
        if (toReturn != ''):
            toReturn = [t] + toReturn
        return toReturn

    def scheduleAt(self, time_to_check):
        toReturn = ''
        t = ''
        for time in self.schedule:
            print(time)
            if (time_in_range(time, time_to_check)):
                print("si")
                toReturn = self.schedule[time]
                t = time
        if (toReturn != ''):
            toReturn = [t] + toReturn
        return toReturn

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)


class URLParser:
    URL_BASE = 'http://wss.math.unipd.it/display/Pages/'
    URL_EXT = '.php'
    XPATH_TO_TABLE_ROWS = '//html/body/table/tbody/tr'
    XPATH_TO_CELLS_CONTENT = './td/h2/text()'
    XPATH_TO_ACTIVITY_TYPE = './td/h3/text()'
    XPATH_IF_NO_LESSONS = "./td[@class='noevent']/text()"

    def parse(self, room):
        url = URLParser.URL_BASE + room + URLParser.URL_EXT
        f = requests.get(url)
        tree = htmllxml.fromstring(f.text)
        rows = tree.xpath(URLParser.XPATH_TO_TABLE_ROWS)
        records = []
        cells = ''
        for row in rows:
            cells = [c for c in row.xpath(
                URLParser.XPATH_IF_NO_LESSONS) if c.strip()]
            res = Results()
            if (len(cells) == 0):
                cells = [c for c in row.xpath(
                    URLParser.XPATH_TO_CELLS_CONTENT) if c.strip()]
                cells += [c for c in row.xpath(
                    URLParser.XPATH_TO_ACTIVITY_TYPE) if c.strip()]
                if (len(cells) > 0):
                    time = html.unescape(cells[0])
                    activity = html.unescape(cells[1])
                    professor = html.unescape(cells[2])
                    if (len(cells) == 3):
                        res = Results(time, activity, professor)
                    elif (len(cells) == 4):
                        activityType = html.unescape(cells[3])
                        res = Results(time, activity, professor, activityType)
            records.append(res)
        return records

    def parseSchedule(self, room):
        return Schedule(room, self.parse(room))


def nowSchedule():
    schedule = ''
    roomActivities = ''
    delimiter = '\t'
    scheduleAccess = ScheduleAccess()
    rooms = retrieve_rooms()
    for room in rooms:
        schedule = scheduleAccess.getScheduleForRoom(room)
        roomScheduleNow = schedule.now()
        roomActivities += '*' + room + '*'
        if (roomScheduleNow != ''):
            for s in roomScheduleNow:
                toAdd = s
                toAdd.replace('_', ' ') \
                    .replace('*', ' ') \
                    .replace('[', ' ') \
                    .replace(']', ' ') \
                    .replace('`', ' ')
                roomActivities += delimiter + toAdd
        else:
            roomActivities += delimiter + "The room is now free"
        roomActivities += '\n'
    return roomActivities


def free_room_parser(strnow = "", hour_min = None):
    schedule = ''
    roomActivities = ''
    nextActivities = []
    scheduleAccess = ScheduleAccess()
    rooms = retrieve_rooms()
    for room in rooms:
        schedule = scheduleAccess.getScheduleForRoom(room)
        roomScheduleNow = schedule.scheduleAt(hour_min) if hour_min else schedule.now()
        if (roomScheduleNow == ''):
            roomActivities += room
            nextActivities = [
                k for k in schedule.schedule if k >= (strnow + '-' + strnow)]
            roomActivities += ' until '
            if (nextActivities != []):
                roomActivities += str(min(nextActivities)).split('-')[0]
            else:
                roomActivities += 'tomorrow'
            roomActivities += '\n'
        elif any(x in roomScheduleNow for x in ["da confermare",
                                                "Aula riservata al Dip.to Matematica"]):
            roomActivities += ("⚠ Possible empty: " + room)
            nextActivities = [
                k for k in schedule.schedule if k >= (strnow + '-' + strnow)]
            roomActivities += ' until '
            if (nextActivities != []):
                roomActivities += str(min(nextActivities)).split('-')[0]
            else:
                roomActivities += 'tomorrow ⚠'
            roomActivities += '\n'
    if (roomActivities != ''):
        return roomActivities
    else:
        return "No room is free"


def freeFrom(hour_min):
    strnow = hour_min.strftime('%H:%M')
    return free_room_parser(strnow, hour_min)


def nowFree():
    tz = pytz.timezone('Europe/Rome')
    now = datetime.datetime.now(tz).time()
    strnow = now.strftime('%H:%M')
    return free_room_parser(strnow)


class ScheduleAccess:
    allSchedules = {}

    def __init__(self):
        if (ScheduleAccess.allSchedules == {}):
            ScheduleUpdater.lookupFromServer()

    def getSchedule(self):
        return ScheduleAccess.allSchedules

    def getScheduleForRoom(self, roomId):
        return ScheduleAccess.allSchedules[roomId]


class ScheduleUpdater:
    def lookupFromServer():
        logging.getLogger().info('Taking data from server')
        parser = URLParser()
        rooms = retrieve_rooms()
        schedule = ''
        for room in rooms:
            schedule = parser.parseSchedule(room)
            ScheduleAccess.allSchedules[room] = schedule


def startUpdater():
    ScheduleUpdater.lookupFromServer()
    if (time(20, 00) <= actual_time() <= time(23, 59)) or \
            (time(2, 00) <= actual_time() <= time(5, 59)):
        threading.Timer(14400, startUpdater).start()
    else:
        threading.Timer(3600, startUpdater).start()
