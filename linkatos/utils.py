import re

yes_re = re.compile("(\s|^)(Yes|YES|yes)(\s|[,.]|$)")
no_re = re.compile("(\s|^)(No|NO|no)(\s|[,.]|$)")


def has_a_yes(message):
    """
    Returns True if it matches the yes regex
    """
    return yes_re.search(message) is not None


def has_a_no(message):
    """
    Returns True if it matches the no regex
    """
    return no_re.search(message) is not None


def from_bot(message, BOT_ID):
    return (message['user'] == BOT_ID)


def has_text(message):
    return ('text' in message)


def has_channel(message):
    return ('channel' in message)


def has_text_keys(message):
    return not ('text' in message and \
                'channel' in message and \
                'ts' in message and \
                'user' in message)


def has_reaction_keys(message):
    return ('reaction' in message and \
            'item' in message and \
            'ts' in message['item'] and \
            'channel' in message['item'] and \
            'user' in message and \
            'item_user' in message)


def is_fresh_url(expecting_confirmation, message_type):
    return (not expecting_confirmation) and message_type is 'url'
