from slackclient import SlackClient

def bot_says(channel, text):
    return slack_client.api_call("chat.postMessage",
                                 channel=channel,
                                 text=text,
                                 as_user=True)


