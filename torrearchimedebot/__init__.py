from bot.telegram_controller import TelegramController
import logging
def main():
    """ Main entry point of the app """
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.getLogger().info('bot started')
    print("TorreArchimedeBot launched.")
    tgController = TelegramController()
    tgController.receiveMessages()
