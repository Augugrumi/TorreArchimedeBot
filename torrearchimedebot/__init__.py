from bot.telegram_controller import TelegramController
def main():
    """ Main entry point of the app """
    print("TorreArchimedeBot launched.")
    tgController = TelegramController()
    tgController.receiveMessages()
