"""
This module includes functions for the bot to display messages Slack.
"""
def bot_says(channel, text, slack_client):
    """
    Posts some text to a specific slack channel.
    """
    return slack_client.api_call("chat.postMessage",
                                 channel=channel,
                                 text=text,
                                 as_user=True)


def compose_explanation(url):
    """
    Composes a message on how to store or ignore the url that has been added to
    the cache.
    """
    return "If you would like {} to be stored please react to it with a :+1:, \
if you would like it to be ignored use :-1:".format(url)


def ask_confirmation(message, slack_client):
    """
    Posts a confirmation message that was composed.
    """
    bot_says(message['channel'],
             compose_explanation(message['url']),
             slack_client)


def compose_list(url_list):
    """
    Composes a response message to a request to list the cache with the list of
    elments in the cache.
    """
    if len(url_list) == 0:
        return "The list is empty"

    intro = "The list of urls to be confirmed is: \n"
    options = ["{} - {}".format(i + 1, v['url']) for i, v in enumerate(url_list)]

    return intro + "\n".join(options)
