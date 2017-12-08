import requests
from lxml import html
import sys
import json

class Results:
    timeStart = ''
    timeEnd = ''
    activity = ''
    professor = ''
    activityType = ''
    
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

url = 'http://wss.math.unipd.it/display/Pages/1A150.php'
if (len(sys.argv) >= 2) :
    url = sys.argv[1]
f = requests.get(url)

#print(f.text)

xpathToTableRows = '//html/body/table/tbody/tr'
xpathToCellContent = './td/h2/text()'
xpathToActivityType = './td/h3/text()'
xpathIfNoLessons = "./td[@class='noevent']/text()"
tree = html.fromstring(f.text)
rows = tree.xpath(xpathToTableRows) #update your table XPath here
records = []
cells = ''
for row in rows:
    cells = [c for c in row.xpath(xpathIfNoLessons) if c.strip()]
    if (len(cells) == 0) :
        cells = [c for c in row.xpath(xpathToCellContent) if c.strip()]
        cells += [c for c in row.xpath(xpathToActivityType) if c.strip()]
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

for r in records:
    print(r)