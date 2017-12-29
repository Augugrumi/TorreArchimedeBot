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

import logging

from bot.telegram_controller import TelegramController
from bot.slack_controller import SlackController
from multiprocessing import Process
def main():
    """ Main entry point of the app """
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.getLogger().info('bot started')

    p1 = Process(target = start_slack)
    p1.start()
    print("TorreArchimedeBot launched.")
    tgController = TelegramController()
    tgController.receiveMessages()

def start_slack():
    sc = SlackController()
