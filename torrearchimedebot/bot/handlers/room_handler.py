from .abs_handler import AbsHandler
from .parsing import *
from .utility import *

class RoomHandler(AbsHandler):

    def __init__(self, roomId):
        self.roomId = roomId

    def handleMessage(self):
        return schedulePrettyfier(ScheduleAccess().getScheduleForRoom(self.roomId))

def schedulePrettyfier(scheduleObj):
    """Take the activity and format it to be displayed in a message"""
    schedule = scheduleObj.getSchedule()
    toReturn = ''
    if (not schedule):
        toReturn = "The room is always empty today!"
    else:
        delimiter = "\t"
        for time in sorted(schedule):

            activity = schedule[time]
            #Check if it is present the activity type
            stop = 2
            if (activity[2] == ''):
                stop = 1

            #Start markdown text modifier
            if (time_in_range(time)):
                toReturn += '* 👉 '
            elif (before_now(time)):
                toReturn += '_'

            #Add all the data
            toReturn += time
            for i in range(0, stop):
                toReturn += delimiter + activity[i] \
                .replace('_', ' ') \
                .replace('*', ' ') \
                .replace('[', ' ') \
                .replace(']', ' ') \
                .replace('`', ' ')

            #End markdown text modifier
            if (time_in_range(time)):
                toReturn += ' 👈 *'
            elif (before_now(time)):
                toReturn += '_'

            toReturn += "\n"
    return toReturn
