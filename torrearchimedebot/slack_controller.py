import os
import time
import re
from slackclient import SlackClient
from bot.handlers.start_handler import StartHandler
from bot.handlers.room_handler import RoomHandler
from bot.handlers.now_handler import NowHandler
from bot.handlers.free_handler import FreeHandler
from bot.handlers.info_handler import InfoHandler
from bot.handlers.utility import *
from bot.handlers.parsing import *

class SlackController:
    # instantiate Slack client
    slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
    # starterbot's user ID in Slack: value is assigned after the bot starts up
    starterbot_id = None

    startUpdater()

    # constants
    RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
    NOW_COMMAND = 'now'
    FREE_COMMAND = 'free'
    MENTION_REGEX = "^<@(|[WU].+)>(.*)"

    def parse_bot_commands(slack_events):
        """
            Parses a list of events coming from the Slack RTM API to find bot commands.
            If a bot command is found, this function returns a tuple of command and channel.
            If its not found, then this function returns None, None.
        """
        for event in slack_events:
            if event["type"] == "message" and not "subtype" in event:
                user_id, message = SlackController.parse_direct_mention(event["text"])
                if user_id == SlackController.starterbot_id:
                    return message, event["channel"]
        return None, None

    def parse_direct_mention(message_text):
        """
            Finds a direct mention (a mention that is at the beginning) in message text
            and returns the user ID which was mentioned. If there is no direct mention, returns None
        """
        matches = re.search(SlackController.MENTION_REGEX, message_text)
        # the first group contains the username, the second group contains the remaining message
        return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

    def handle_command(command, channel):
        """
            Executes bot command if the command is known
        """
        # Default response is help text for the user
        default_response = "Not sure what you mean."

        # Finds and executes the given command, filling in response
        response = None
        handler = None
        if command.startswith(SlackController.NOW_COMMAND):
            handler = NowHandler()
        elif command.startswith(SlackController.FREE_COMMAND):
            handler = FreeHandler()
        else:
            roomId = ''
            messageRoom = command.split(' ')[0]
            for r in retrieve_rooms():
                if r.upper() == messageRoom.upper():
                    roomId = r
            handler = RoomHandler(roomId)
        response = handler.handleMessage()

        # Sends the response back to the channel
        SlackController.slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=response or default_response
        )

    def __init__(self):
        if SlackController.slack_client.rtm_connect(with_team_state=False):
            print("Starter Bot connected and running!")
            # Read bot's user ID by calling Web API method `auth.test`
            SlackController.starterbot_id = SlackController.slack_client.api_call("auth.test")["user_id"]
            while True:
                command, channel = SlackController.parse_bot_commands(SlackController.slack_client.rtm_read())
                if command:
                    SlackController.handle_command(command, channel)
                time.sleep(SlackController.RTM_READ_DELAY)
        else:
            print("Connection failed. Exception traceback printed above.")