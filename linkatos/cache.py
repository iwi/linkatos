from . import printer

def is_url(element):
"""
Checks if the input is not `None`.
The input is supposed to be a Slack event, but that's currently not verified.
"""
    return element is not None


def is_not_from_bot(bot_id, user_id):
"""
Compares two bot ids and verifies that they're different.

is this really necessary??
"""
    return not bot_id == user_id


def is_empty(xs):
"""
Checks if the cache is empty. Currently the cache is implemented as a list
therefore it's only necessary to check if the list is empty.
"""
    return len(xs) == 0


def add(element, cache, slack_client):
"""
Adds an element to the cache, appending it to the end of it.
And sends a message requesting confirmation.
"""
    cache.append(element)
    printer.ask_confirmation(element, slack_client)
    return cache


def extract_url_by_id(cache, reaction_to_id):
"""
Extracts a url from the cache based on its identifier ('id') which comes from
the slack message time-stamp.

Extracting means getting it and deleting it from the cache.
"""
    for index in range(0, len(cache)):
        if cache[index]['id'] == reaction_to_id:
            element = cache[index]
            cache.pop(index)
            return element

    # if not found
    return None


def extract_url_by_index(cache, index):
"""
Extracts a url from the cache based on its position in it.
"""
    if (index > len(cache) - 1) or (index < 0):
        return None

    element = cache[index]
    cache.pop(index)
    return element


def display(cache, channel, slack_client):
"""
Displays the list of elements in the cache to a specific channel in Slack.
"""
    printer.bot_says(channel,
                     printer.compose_list(cache),
                     slack_client)
