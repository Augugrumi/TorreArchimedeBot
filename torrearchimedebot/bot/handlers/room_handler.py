from .abs_handler import AbsHandler
from .parsing import *
import datetime

class RoomHandler(AbsHandler):

    def __init__(self, roomId):
        self.roomId = roomId

    def handleMessage(self):
        return schedulePrettyfier(URLParser().parseSchedule(self.roomId))

def schedulePrettyfier(scheduleObj):
    """Take the activity and format it to be displayed in a message"""
    schedule = scheduleObj.getSchedule()
    toReturn = ''
    if (not schedule):
        toReturn = "The room is always empty today!"
    else:
        delimiter = "\t"
        for time in schedule:

            activity = schedule[time]
            #Check if it is present the activity type
            stop = 2
            if (activity[2] == ''):
                stop = 1

            #Start markdown text modifier
            if (time_in_range(time)):
                toReturn += '*> '
            elif (before_now(time)):
                toReturn += '_'

            #Add all the data
            toReturn += time
            for i in range(0, stop):
                toReturn += delimiter + activity[i]
            
            #End markdown text modifier
            if (time_in_range(time)):
                toReturn += ' <*'
            elif (before_now(time)):
                toReturn += '_'
            
            toReturn += "\n" 
    return toReturn

def time_in_range(interval):
    """Return true if the interval include actual time"""
    [start, end] = string_interval_to_time(interval)
    now = datetime.datetime.now().time()
    if start <= end:
        return start <= now <= end
    else:
        return start <= now or now <= end

def before_now(interval):
    """Return true if the interval is ended before actual time"""
    [start, end] = string_interval_to_time(interval)
    now = datetime.datetime.now().time()
    return now > end

def string_interval_to_time(interval):
    """Return 2 time retrieved from the string interval"""
    [timeStart, timeEnd] = interval.split('-')
    [startHour, startMin] = timeStart.split(':')
    [endHour, endMin] = timeEnd.split(':')
    start = datetime.time(int(startHour), int(startMin), 0)
    end = datetime.time(int(endHour), int(endMin), 0)
    return [start, end]

#print(RoomHandler('1A150').handleMessage())