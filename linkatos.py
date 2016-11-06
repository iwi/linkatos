import os
import time
from slackclient import SlackClient
import re

# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")

# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"
WEB_LINK = "http"
website_pattern = "https?://\S+(\s|$)"
prog = re.compile(website_pattern)

# instantiate Slack & Twilio clients
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


def bot_message (channel, text) :
    return slack_client.api_call("chat.postMessage", 
                                 channel = channel,
                                 text = text,
                                 as_user = True)

def handle_command(command, channel) :
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
               "* command with numbers, delimited by spaces."
    if command.startswith(EXAMPLE_COMMAND) :
        response = "Sure...write some more code then I can do that!"
    
    bot_message(channel, response)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    print output_list
    if output_list and len(output_list) > 0 :
        for output in output_list :
            if output and 'text' in output and AT_BOT in output['text'] :
                slack_client.api_call("chat.postMessage", 
                    channel = output['channel'], 
                    text = "r u talkin' to me?",
                    as_user = True)
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                     output['channel']
            elif output and \
                    'text' in output and \
                    prog.search(output['text']) != None and \
                    output['user'] !=  BOT_ID :
                response = "It looks like you posted a link. /n \
                    The link is: " + prog.search(output['text']).group(0)
                bot_message(output['channel'], response)
                # return text after the @ mention, whitespace removed
                return output['text'].strip().lower(), output['channel']
    return None, None


if __name__ == "__main__" :
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect() :
        print("linkatos is connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else :
        print("Connection failed. Invalid Slack token or bot ID?")
