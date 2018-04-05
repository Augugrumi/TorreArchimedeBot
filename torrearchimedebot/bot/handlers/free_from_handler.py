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


class FreeFromHandler(AbsHandler):

    def __init__(self, message):
        self._message = message

    def handleMessage(self):
        # "\freefrom " is 10 characters
        string_time = parse_freefrom_time(self._message[10:])
        if not type(string_time) is datetime.time:
            return string_time
        response = freeFrom(string_time)
        return "Rooms that are free from " + string_time.strftime('%H:%M') \
               + " are:\n" + response
