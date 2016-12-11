#! /usr/bin/env python
import os
import time
from slackclient import SlackClient
import pyrebase
import linkatos.parser as parser
import linkatos.confirmation as confirmation
import linkatos.printer as printer
import linkatos.utils as utils
import linkatos.firebase as fb

# starterbot environment variables
BOT_ID = os.environ.get("BOT_ID")
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")

# instantiate Slack clients
slack_client = SlackClient(SLACK_BOT_TOKEN)

# firebase environment variables
FB_API_KEY = os.environ.get("FB_API_KEY")
FB_USER = os.environ.get("FB_USER")
FB_PASS = os.environ.get("FB_PASS")

# initialise firebase
project_name = 'coses-acbe6'
firebase = fb.initialise(FB_API_KEY, project_name)


# Main
if __name__ == '__main__':
    READ_WEBSOCKET_DELAY = 1  # 1 second delay between reading from firehose

    # verify linkatos connection
    if slack_client.rtm_connect():
        expecting_confirmation = False
        url = None

        while True:
            (expecting_confirmation, url) = do.keep_wanted_urls(expecting_confirmation, url)

    else:
        print("Connection failed. Invalid Slack token or bot ID?")
