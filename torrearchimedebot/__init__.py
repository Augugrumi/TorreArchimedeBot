from bot.telegram_controller import TelegramController
import logging
from slack_controller import SlackController
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