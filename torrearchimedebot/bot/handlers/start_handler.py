from .abs_handler import AbsHandler

class StartHandler(AbsHandler):

    def handleMessage(self):
        return "Hey! I'm the Archimede Tower. Do you want to see the " + \
    "scheduling of a particolar room? Type /<roomName>!"
