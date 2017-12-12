from telegram.ext import Updater
from telegram.ext import CommandHandler
from bot.handlers.start_handler import StartHandler
from bot.handlers.room_handler import RoomHandler
from bot.handlers.now_handler import NowHandler
from bot.handlers.free_handler import FreeHandler
from bot.handlers.info_handler import InfoHandler
from .handlers.utility import *
import os

class TelegramController:

    def __init__(self):
        self._updater = Updater(token=os.environ['TG_TOKEN'])
        self._dispatcher = self._updater.dispatcher

        # Start Handler
        startHandler = CommandHandler('start', self.start)
        self._dispatcher.add_handler(startHandler)

        #Now Handler
        nowHandler = CommandHandler('now', self.now)
        self._dispatcher.add_handler(nowHandler)

        #Free rooms Handler
        freeHandler = CommandHandler('free', self.free)
        self._dispatcher.add_handler(freeHandler)

        #Info handler
        infoHandler = CommandHandler('info', self.info)
        self._dispatcher.add_handler(infoHandler)

        # Room Handlers definitions
        rooms = retrieve_rooms()
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

    def now(self, bot, update):
        handler = NowHandler()
        bot.send_message(parse_mode='Markdown', chat_id=update.message.chat_id, text=handler.handleMessage())

    def free(self, bot, update):
        handler = FreeHandler()
        bot.send_message(chat_id=update.message.chat_id, text=handler.handleMessage())

    def info(self, bot, update):
        handler = InfoHandler()
        bot.send_message(parse_mode='Markdown', chat_id=update.message.chat_id, text=handler.handleMessage())
