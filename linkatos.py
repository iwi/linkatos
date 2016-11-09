import os
import time
from slackclient import SlackClient
import re

# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN"))

# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"

# instantiate Slack & Twilio clients
slack_client = SlackClient(SLACK_BOT_TOKEN)


def bot_says (channel, text) :
    return slack_client.api_call("chat.postMessage",
                                 channel = channel,
                                 text = text,
                                 as_user = True)


def store_link (link, channel) :
    """
        Receives a link.
        Stores it in the db.
        Sends a confirmation message.
    """

    error = db.store(link)
    message = "Success! The link has been stored"

    if error :
        message = "ERROR: the link could not be stored"

    bot_says(channel, message)

    return None


def message_contains_link (message) :
    """
    Returns a link if it matches the regex
    """
    website_pattern = "https?://\S+(\s|$)"
    prog = re.compile(website_pattern)
    return prog.search(output['text']).strip() 


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless
        someone posts a website link starting with httpS?//

        In these situations the function will return the link and the channel 
        where the message was posted.

    """

    # default outcome
    link = None
    channel = None

    output_list = slack_rtm_output
    print output_list  # print the list of outputs to get them on screen

    if output_list and len(output_list) > 0 :
        for output in output_list :
            # when there is a message then get the channel
            if channel : channel = output['channel']

            if output and output['text'] and output['user'] != BOT_ID :
                link = message_contains_a_link(output['text'])            

            if message_contains_a_link(text) :
                link = message_contains_a_link(text)
                response = "It looks like you posted a link. \
                    The link is: " + link.group(0)
                bot_says(channel,
                         "It looks like you posted a link. \
                             The link is: " + link.group(0)

    return link, channel


if __name__ == '__main__' :
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    # verify linkatos connection
    if slack_client.rtm_connect() :
        print "linkatos is connected and running!"
        while True:
            print "linkatos is listening"

            # parse the messages. Get 'None' while they're empty
            link, channel = parse_slack_output(slack_client.rtm_read())

            # handle the command when it is a http address
            if link and channel :
                bot_says(channel, "Do you want me to store the link " + \
                        link + " for you?") 
                
                # parse answerif answer...
                response = parse_response_from_user(slack_client.rtm_read())
                if response :
                    store_link(link)

            time.sleep(READ_WEBSOCKET_DELAY)

    else :
        print "Connection failed. Invalid Slack token or bot ID?"

