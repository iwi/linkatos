import re

url_re = re.compile("(?:\s|^)<(https?://[\w./?+&+%$!#=\-_]+)>(?:\s|$)")

def extract_url(message):
    """
    Returns the first url in a message. If there aren't any returns None
    """
    answer = url_re.search(message)

    if answer is not None:
        answer = answer.group(1).strip()

    return answer


def to_bot(message, bot_id):
    # to find a message to the bot
    bot_re = "^<@" + bot_id + '>'
    to_bot_re = re.compile(bot_re)

    return to_bot_re.search(message).group(0) is not None


def is_list_request(message):
    list_re = re.compile("list")
    return list_re.search(message).group(0) == 'list'
