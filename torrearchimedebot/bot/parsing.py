import requests
from lxml import html
import sys
import json

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
                    print(Results)
                elif (len(cells)==3):
                    records.append(Results(cells[0], cells[1], cells[2]))
                    print(Results(cells[0], cells[1], cells[2]))
                elif (len(cells)==4):
                    records.append(Results(cells[0], cells[1], cells[2], cells[3]))
                    print(Results(cells[0], cells[1], cells[2], cells[3]))
            else :
                records.append(Results())
        return records

    def parseSchedule(self, room):
        return Scedule(room, self.parse(room))

schedule = URLParser().parseSchedule('1A150')
print(schedule)