from . import firebase as fb


def positive_reaction(reaction):
    return reaction == '+1'


def is_known(reaction):
    return reaction in ['+1', '-1']


def extract_url_by_id(cache, reaction_to_id):
    for index in range(0, len(cache)):
        if cache[index]['id'] == reaction_to_id:
            element = cache[index]
            cache.pop(index)
            return element

    # if not found
    return None


def extract_url_by_index(cache, index):
    if (index > len(cache) - 1) or (index < 0):
        return None

    element = cache[index]
    cache.pop(index)
    return element


def handle(reaction, url, fb_credentials, firebase):
    if positive_reaction(reaction):
        fb.connect_and_store_url(url, fb_credentials, firebase)
