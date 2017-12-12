from .abs_handler import AbsHandler
from .parsing import *

class NowHandler(AbsHandler):

    def handleMessage(self):
        return nowSchedule()
