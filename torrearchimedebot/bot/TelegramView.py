from telegram.ext import Updater
from telegram.ext import CommandHandler
import os

class TelegramView:
    updater = Updater(token=os.environ['DEBUSSY'])
    dispatcher = updater.dispatcher
