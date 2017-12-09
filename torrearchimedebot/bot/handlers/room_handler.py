from .abs_handler import AbsHandler
from ../parsing import *

class RoomHandler(AbsHandler):

    def __init__(self, roomId):
        self.roomId = roomId

    def handleMessage(self):
        return schedulePrettyfier(URLParser().parseSchedule(self.roomId))

    def schedulePrettyfier(scheduleObj):
        schedule = scheduleObj.getSchedule()
        toReturn = ''
        if (not schedule):
            toReturn = "The room is always empty today!"
        else:
            delimiter = "  "
            for time in schedule:
                activity = schedule[time]
                stop = 2
                if (activity[2] == '')
                    stop = 1
                toReturn += time
                for i in range(0, stop):
                    toReturn = delimiter + activity[i]
                toReturn += "\n" 
        return toReturn
