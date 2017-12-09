from .abs_handler import AbsHandler

class RoomHandler(AbsHandler):

    def __init__(self, roomId):
        self.roomId = roomId

    def handleMessage(self):
        return "Scheduling for " + self.roomId + ": WIP"
