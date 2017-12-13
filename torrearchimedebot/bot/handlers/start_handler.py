from .abs_handler import AbsHandler

class StartHandler(AbsHandler):

    def handleMessage(self):
        return "Hey! 👋 I'm the Archimede Tower 🏢.\nDo you want to see the " + \
    "scheduling of a particolar room? 🕛 Type /<roomName>!\nTo see free " + \
    "rooms just type /free and to see coming events type /now ⏰\n" + \
    "Want to know more about this bot? ©️ Type /info!"
