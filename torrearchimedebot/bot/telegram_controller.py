from telegram.ext import Updater
from telegram.ext import CommandHandler
from handlers.start_handler import StartHandler
import os

class TelegramController:

    def __init__(self):
        self._updater = Updater(token=os.environ['TG_TOKEN'])
        self._dispatcher = self._updater.dispatcher
        // Start Handler
        start_handler = CommandHandler('start', self.start)
        self._dispatcher.add_handler('start', start_handler)

    def start(self, bot, update) :
        handler = StartHandler()
        bot.send_message(chat_id=update.message.chat_id, text=handler.handleMessage())
