from . import firebase as fb


def positive_reaction(reaction):
"""
Checks if a reaction is positive. That is if it is :+1:
"""
    return reaction == '+1'


def is_known(reaction):
"""
Checks if a reaction is known. That is if it is either :+1: or :-1:
"""
    return reaction in ['+1', '-1']


def extract_url_by_id(cache, reaction_to_id):
"""
Extracts a url from the cache based on its identifier ('id') which comes from
the slack message time-stamp.

Extracting means getting it and deleting it from
the cache.
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


def handle(reaction, url, fb_credentials, firebase):
"""
Handles a reaction to a specific url. That is storing the url or ignoring it
depending on the reaction.
"""
    if positive_reaction(reaction):
        fb.connect_and_store_url(url, fb_credentials, firebase)
