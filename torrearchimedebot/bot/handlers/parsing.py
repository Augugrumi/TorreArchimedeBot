import requests
from lxml import html
import sys
import json
from utility import *

class Results:
    def __init__(self, time = '', activity = '', professor = '', activityType = ''):
        if (time != '') :
            [timeStart, timeEnd] = time.split(' - ')
            self.timeStart = timeStart
            self.timeEnd = timeEnd
        else :
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

def  json2Schedule(jsonString):
    print(jsonString)
    data = json.loads(jsonString)
    schedule = data["schedule"]
    results = []
    for r in schedule:
        key = r
        r = r.replace("-", " - ")
        results.append(Results(r, schedule[key][0], schedule[key][1], schedule[key][2]))
    return Scedule(data["room"], results)



class Scedule:
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
        tree = html.fromstring(f.text)
        rows = tree.xpath(URLParser.XPATH_TO_TABLE_ROWS)
        records = []
        cells = ''
        for row in rows:
            cells = [c for c in row.xpath(URLParser.XPATH_IF_NO_LESSONS) if c.strip()]
            if (len(cells) == 0) :
                cells = [c for c in row.xpath(URLParser.XPATH_TO_CELLS_CONTENT) if c.strip()]
                cells += [c for c in row.xpath(URLParser.XPATH_TO_ACTIVITY_TYPE) if c.strip()]
                if (len(cells)<=0):
                    records.append(Results())
                    #print(Results)
                elif (len(cells)==3):
                    records.append(Results(cells[0], cells[1], cells[2]))
                    #print(Results(cells[0], cells[1], cells[2]))
                elif (len(cells)==4):
                    records.append(Results(cells[0], cells[1], cells[2], cells[3]))
                    #print(Results(cells[0], cells[1], cells[2], cells[3]))
            else :
                records.append(Results())
        return records

    def parseSchedule(self, room):
        return Scedule(room, self.parse(room))

def nowSchedule():
    parser = URLParser()
    rooms = retrieve_rooms()
    schedule = ''
    roomActivities = ''
    delimiter = '\t'
    for room in rooms:
        schedule = parser.parseSchedule(room)
        roomSceduleNow = schedule.now()
        roomActivities += '*' + room + '*' 
        if (roomSceduleNow != ''):
            for s in roomSceduleNow:
                roomActivities += delimiter + s
        else:
            roomActivities += delimiter + "The room is now free"
        roomActivities += '\n'
    return roomActivities

def nowFree():
    parser = URLParser()
    rooms = retrieve_rooms()
    schedule = ''
    roomActivities = ''
    delimiter = '\t'
    for room in rooms:
        schedule = parser.parseSchedule(room)
        roomSceduleNow = schedule.now()
        if (roomSceduleNow == ''):
            roomActivities += room
            roomActivities += '\n'
    if (roomActivities != ''):
        return roomActivities
    else:
        return "No room is free"
