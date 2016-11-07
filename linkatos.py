import os
import time
from slackclient import SlackClient
import re

# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")

# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"

# instantiate Slack & Twilio clients
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


def bot_says (channel, text) :
    return slack_client.api_call("chat.postMessage",
                                 channel = channel,
                                 text = text,
                                 as_user = True)

def handle_command (command, channel) :
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
               "* command with numbers, delimited by spaces."
    if command.startswith(EXAMPLE_COMMAND) :
        response = "Sure...write some more code then I can do that!"

    bot_says(channel, response)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless:
        1. a message is directed at linkatos, based on its ID.
        2. someone posts a website link starting with http

        In these situations the function will return the channel where
        the message was posted and the relevant information from the message.

        Maybe worth including a flag for the type of outcome?

    """
    # default outcom
    command = None
    channel = None
    message_is_addressed_to_bot = None

    output_list = slack_rtm_output
    print output_list  # print the list of outputs to get them on screen

    if output_list and len(output_list) > 0 :
        for output in output_list :
            # when there is a message then get the channel
            if channel : channel = output['channel']

            # if the message is directed to linkatos
            message_is_addressed_to_bot = output and \
                    'text' in output and \
                    AT_BOT in output['text'] 

            if message_is_addressed_to_bot :
                bot_says(output['channel'], "r u talkin' to me?")
                command = output['text'].split(AT_BOT)[1].strip().lower()

            # if the message contains a link
            # determine the filter
            website_pattern = "https?://\S+(\s|$)"
            prog = re.compile(website_pattern)

            if output and \
                    'text' in output and \
                    prog.search(output['text']) != None and \
                    output['user'] !=  BOT_ID : # avoid linkatos messages

                response = "It looks like you posted a link. \
                    The link is: " + prog.search(output['text']).group(0)
                bot_says(output['channel'], response)
                # return text after the @ mention, whitespace removed
                command = output['text'].strip().lower()

    return command, channel, message_is_addressed_to_bot


if __name__ == "__main__" :
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    # verify linkatos connection
    if slack_client.rtm_connect() :
        print "linkatos is connected and running!"
        while True:
            print "linkatos listening"
            # parse the messages and get 'None' while they're empty
            command, channel, message_is_addressed_to_bot = \
                    parse_slack_output(slack_client.rtm_read())

            # handle the command when it is addressed to linkatos
            if message_is_addressed_to_bot and command and channel:
                handle_command(command, channel)

            time.sleep(READ_WEBSOCKET_DELAY)

    else :
        print "Connection failed. Invalid Slack token or bot ID?"

