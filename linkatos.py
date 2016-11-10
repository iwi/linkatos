#! /bin/env python
import os
import time
from slackclient import SlackClient
import re

# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")

# instantiate Slack clients
slack_client = SlackClient(SLACK_BOT_TOKEN)


def bot_says (channel, text):
    return slack_client.api_call("chat.postMessage",
                                 channel=channel,
                                 text=text,
                                 as_user=True)


def store_link (link, channel):
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


def message_contains_a_link (message):
    """
    Returns a link if it matches the regex
    """
    answer = link_re.search(message)
    if answer is not None:
        answer = answer.group(0).strip()

    return answer



def message_contains_a_yes (message):
    """
    Returns a link if it matches the regex
    """
    answer = yes_re.search(message)
    if answer is not None:
        answer = answer.group(0).strip()

    return answer


def parse_output (slack_rtm_output, link_re):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless
        someone posts a website link starting with httpS?// or a yes
    """
    # default outcome
    finding = None
    channel = None
    output_type = None

    output_list = slack_rtm_output
    print(output_list)  # print the list of outputs to get them on screen

    if output_list and len(output_list) > 0:
        for output in output_list:
            # when there is a message then get the channel
            if output and 'text' in output and output['user'] != BOT_ID:
                finding = message_contains_a_link(output['text'])
                if finding is not None:
                    print(finding)
                    output_type = 'link' 
                else:
                    finding = message_contains_a_yes(output['text'])
                    if finding is not None:
                        output_type = 'yes' 

            if output and 'channel' in output:
                channel = output['channel']


    return (finding, channel, output_type)


if __name__ == '__main__':
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    # Precompile regex patterns
    link_re = re.compile("https?://\S+(\s|$)")
    yes_re = re.compile("[Yy][eE].[sS].")

    # verify linkatos connection
    if slack_client.rtm_connect():
        print("linkatos is connected and running!")

        while True:
            print("linkatos is listening")

            # parse the messages. Get 'None' while they're empty
            (link, channel, output_type) = parse_output(slack_client.rtm_read(), link_re)

            # handle the command when it is a http address
            if link is not None and output_type is 'link' and channel:
                bot_says(channel, "Do you want me to store the link " + \
                        link + " for you?")

                # parse answerif answer...
                (answer, channel, output_type) = \
                    parse_output(slack_client.rtm_read(), yes_re)

                # just to debug
                if answer is not None:
                    print("you said Yes")

                #if response:
                #    store_link(link)

            time.sleep(READ_WEBSOCKET_DELAY)

    else:
        print("Connection failed. Invalid Slack token or bot ID?")

