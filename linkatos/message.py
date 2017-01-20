import re


def extract_url(message):
    """
    Finds the first url within a text and if it exists it returns it.
    """
    # Returns the first url in a message. If there aren't any returns None
    url_re = "(?:\s|^)<(https?://[\w./?+&+%$!#=\-_]+)>(?:\s|$)"
    captures = re.search(url_re, message)

    if captures is not None:
        captures = captures.group(1).strip()

    return captures


def to_bot(message, bot_id):
    """
    Checks if a message is directed to a specific bot_id. That is, contains
    '@<bot_id\>'
    """
    bot_re = "^<@" + bot_id + '>'
    bot_found = re.search(bot_re, message)

    return bot_found is not None


def is_list_request(message):
    """
    Checks if a message contains 'list'.
    """
    list_found = re.search("list", message)

    return list_found is not None


def purge_request(message):
    """
    Checks if a message contains 'purge' and has a number afterwards.
    """
    index_found = re.search("(purge) (\d+)", message)

    if index_found is None:
        return None

    return int(index_found.group(2))
