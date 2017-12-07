import requests
from lxml import html
import sys

class Results:
    def __init__(self, time, activity, professor, activityType):
        [timeStart, timeEnd] = time.split(' - ')
        self.timeStart = timeStart
        self.timeEnd = timeEnd
        self.activity = activity
        self.professor = professor
        self.activityType = activityType
   
    def __init__(self, time, activity, professor):
        [timeStart, timeEnd] = time.split(' - ')
        self.timeStart = timeStart
        self.timeEnd = timeEnd
        self.activity = activity
        self.professor = professor
        self.activityType = ''
    
    

url = 'http://wss.math.unipd.it/display/Pages/1A150.php'
if (sys.argv[1] != "") :
    url = sys.argv[1]
f = requests.get(url)

print(f.text)

tree = html.fromstring(f.text)
rows = tree.xpath('//html/body/table/tbody/tr') #update your table XPath here
records = []
for row in rows:
    cells = [c for c in row.xpath('./td/h2/text()') if c.strip()]
    cells += [c for c in row.xpath('./td/h3/text()') if c.strip()]
    if (len(cells)>0):
        if (len(cells)==3):
            print(Results(cells[0], cells[1], cells[2]))
        if (len(cells)==4):
            print(Results(cells[0], cells[1], cells[2], cells[3]))

    else:
        print(Results())
