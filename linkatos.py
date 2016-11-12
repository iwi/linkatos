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


def parse_output(slack_rtm_output):
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
                finding = message.extract_url(output['text'])
                if finding is not None:
                    output_type = 'link'
                else:
                    if message.has_a_yes(output['text']):
                        output_type = 'yes'

            if output and 'channel' in output:
                channel = output['channel']

    return (finding, channel, output_type)


if __name__ == '__main__':
    READ_WEBSOCKET_DELAY = 1  # 1 second delay between reading from firehose

    # verify linkatos connection
    if slack_client.rtm_connect():
        print("linkatos is connected and running!")

        while True:
            print("linkatos is listening")

            # parse the messages. Get 'None' while they're empty
            messages = slack_client.rtm_read()
            (link, channel, output_type) = parse_output(messages)

            # handle the command when it is a http address
            if link is not None and output_type is 'link' and channel:
                bot_says(channel, "Do you want me to store the link " +
                         link + " for you?")

                # parse answerif answer...
                messages = slack_client.rtm_read()
                (answer, channel, output_type) = parse_output(messages)
                print(answer)

                # just to debug
                if answer is not None:
                    print("you said Yes")

                # if response:
                #     store_link(link)

            time.sleep(READ_WEBSOCKET_DELAY)

    else:
        print("Connection failed. Invalid Slack token or bot ID?")
