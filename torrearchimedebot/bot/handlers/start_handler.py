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

class StartHandler(AbsHandler):

    def handleMessage(self):
        return "Hey! 👋 I'm the Archimede Tower 🏢.\nDo you want to see the " + \
    "scheduling of a particolar room? 🕛 Type /<roomName>!\nTo see free " + \
    "rooms just type /free and to see coming events type /now ⏰\n" + \
    "Want to know more about this bot? ©️ Type /info!"
