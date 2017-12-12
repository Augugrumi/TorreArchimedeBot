from .abs_handler import AbsHandler
from .parsing import *

class FreeHandler(AbsHandler):

    def handleMessage(self):
        return "Rooms that now are free:\n" + nowFree()
