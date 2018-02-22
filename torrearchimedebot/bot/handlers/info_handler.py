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


class InfoHandler(AbsHandler):

    def __init__(self):
        self.github = "https://github.com/Augugrumi/TorreArchimedeBot"
        self.url_donation = "http://paypal.me/DavidePolonio"
        self.author = "Augugrumi Team"
        self.version = "0.3.7"

    def handleMessage(self):

        return "*Torre Archimede Bot*, version `" + self.version + \
            "`.\n_Brought to you with ❤️ by " + self.author + "_.\n" + \
            "Do you want to contribute or report an issue? You can find us" + \
            " at: " + self.github + "!\n\nEveryone knows that programmers " + \
            "are machines able to transform coffee into code. Please " + \
            "help us buying some! \n" + self.url_donation
