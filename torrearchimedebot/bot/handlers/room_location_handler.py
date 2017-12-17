from .abs_handler import AbsHandler

class RoomLocationHandler(AbsHandler):

    ROOM_URL_LOCATION = "http://wss.math.unipd.it/display/Pages/img/"
    IMAGE_EXTENSION = ".png"

    def __init__(self, roomId):
        self.roomId = roomId

    def handleMessage(self):
        return RoomLocationHandler.ROOM_URL_LOCATION + \
               self.roomId + \
               RoomLocationHandler.IMAGE_EXTENSION
