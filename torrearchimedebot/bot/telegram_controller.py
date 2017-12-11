from telegram.ext import Updater
from telegram.ext import CommandHandler
from bot.handlers.start_handler import StartHandler
from bot.handlers.room_handler import RoomHandler
import os

class TelegramController:

    def __init__(self):
        self._updater = Updater(token=os.environ['TG_TOKEN'])
        self._dispatcher = self._updater.dispatcher
        # Start Handler
        startHandler = CommandHandler('start', self.start)
        self._dispatcher.add_handler(startHandler)

        # Room Handlers definitions
        # FIXME: we need to save this list in some place outside this class
        rooms = [
        '1A150',
        '1AD100',
        '1BC45',
        '1BC50',
        '1C150',
        '1AD100',
        '2AB40',
        '2AB45',
        '2BC30',
        '2BC60',
        'LabTA'
        ]
        for room in rooms:
            handler = CommandHandler(room, self.roomSchedule)
            self._dispatcher.add_handler(handler)

    def receiveMessages(self):
        self._updater.start_polling()

    def start(self, bot, update):
        handler = StartHandler()
        bot.send_message(chat_id=update.message.chat_id, text=handler.handleMessage())

    def roomSchedule(self, bot, update):
        handler = RoomHandler(update.message.text[1:])
        bot.send_message(parse_mode='Markdown', chat_id=update.message.chat_id, text=handler.handleMessage())
