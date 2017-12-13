from .abs_handler import AbsHandler

class InfoHandler(AbsHandler):

    def __init__(self):
        self.github = "https://github.com/Augugrumi/TorreArchimedeBot"
        self.url_donation = "http://paypal.me/DavidePolonio"
        self.author = "Augugrumi Team"
        self.version = "0.1.3"

    def handleMessage(self):

        return "*Torre Archimede Bot*, version `" + self.version + \
    "`.\n_Brought to you with ❤️ by " + self.author + "_.\n" + \
    "Do you want to contribute or report an issue? You can find us at: " + \
    self.github + "!\n\nEveryone knows that programmers are machines able to " + \
    "transform coffee into code. Please help us buying some! \n" + \
    self.url_donation
