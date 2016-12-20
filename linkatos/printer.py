from .utils import is_fresh_url


def bot_says(channel, text, slack_client):
    return slack_client.api_call("chat.postMessage",
                                 channel=channel,
                                 text=text,
                                 as_user=True)


def compose_explanation(url):
    return "If you would like {} to be stored please react to it with a :+1:".format(url)


def ask_confirmation(parsed_message, slack_client):
    bot_says(parsed_message['channel'],
             compose_explanation(parsed_message['message']),
             slack_client)
