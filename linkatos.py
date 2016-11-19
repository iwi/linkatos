#! /usr/bin/env python
import os
import time
from slackclient import SlackClient
import linkatos.parser as parser
import linkatos.confirmation as confirmation
import linkatos.printer as printer

# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")

# instantiate Slack clients
slack_client = SlackClient(SLACK_BOT_TOKEN)

def store_link(link, channel):
    """
     ------------------- INACTIVE FUNCTION
        Receives a link.
        Stores it in the db.
        Sends a confirmation message.
    """
    error = db.store(link)
    message = "Success! The link has been stored"

    if error:
        message = "ERROR: the link could not be stored"

    printer.bot_says(channel, message)

    return None

# Main
if __name__ == '__main__':
    READ_WEBSOCKET_DELAY = 1  # 1 second delay between reading from firehose

    # verify linkatos connection
    if slack_client.rtm_connect():
        print("linkatos is connected and running!")
        expecting_confirmation = False

        while True:
            print("linkatos is listening")

            # parse the messages. Get a dictionary with @out, @channel,
            # @out_type
            parsed_message = parser.parse(slack_client.rtm_read(), BOT_ID)

            # update expecting_confirmation
            # when it's a url
            expecting_confirmation = confirmation.update_confirmation_if_url(
                                                    parsed_message,
                                                    expecting_confirmation)

            # when it's the answer after a url
            expecting_confirmation = confirm.process_confirmation_if_yn(
                                                    parsed_message,
                                                    expecting_confirmation)

            time.sleep(READ_WEBSOCKET_DELAY)

    else:
        print("Connection failed. Invalid Slack token or bot ID?")
