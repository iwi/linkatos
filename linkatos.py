#! /usr/bin/env python
import os
import time
from slackclient import SlackClient
import linkatos.message as message


# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")

# instantiate Slack clients
slack_client = SlackClient(SLACK_BOT_TOKEN)


def bot_says(channel, text):
    return slack_client.api_call("chat.postMessage",
                                 channel=channel,
                                 text=text,
                                 as_user=True)


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

    bot_says(channel, message)

    return None


if __name__ == '__main__':
    READ_WEBSOCKET_DELAY = 1  # 1 second delay between reading from firehose

    # verify linkatos connection
    if slack_client.rtm_connect():
        print("linkatos is connected and running!")
        expecting_confirmation = False

        while True:
            print("linkatos is listening")

            # parse the messages. Get 'None' while they're empty
            (out, channel, out_type) = message.parse(slack_client.rtm_read())

            # handle the command when it is a url
            if out is not None  and channel:
                if expecting_confirmation is False and out_type is 'url':
                    url = out
                    expecting_confirmation = True
                    bot_says(channel, "Do you want me to store the link " +
                         url + " for you?")
                elif expecting_confirmation is True and out_type is 'yn_answer':
                    is_yes = out
                    expecting_confirmation = False
                    if is_yes is True:
                        # store_url(link) # function not yet ready
                        bot_says(channel, url + " has been stored")

            time.sleep(READ_WEBSOCKET_DELAY)

    else:
        print("Connection failed. Invalid Slack token or bot ID?")
