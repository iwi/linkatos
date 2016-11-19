from .utils import is_fresh_url


def bot_says(channel, text, slack_client):
    return slack_client.api_call("chat.postMessage",
                                 channel=channel,
                                 text=text,
                                 as_user=True)


def compose_question(url):
    return "Do you want me to store the link {} for you?".format(url)


def ask_confirmation(expecting_confirmation, parsed_message, slack_client):
    print('asking')
    if is_fresh_url(expecting_confirmation, parsed_message['type']):
        bot_says(parsed_message['channel'],
                 compose_question(parsed_message['out']),
                 slack_client)
