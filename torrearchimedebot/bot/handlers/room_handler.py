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
