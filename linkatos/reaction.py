from . import firebase as fb


def positive_reaction(reaction):
    return reaction == '+1'


def known_reaction(reaction):
    return reaction in ['+1', '-1']


def get_index(url_cache_list, reaction_to_id):
    for index in range(0, len(url_cache_list) - 1):
        if url_cache_list[index]['id'] == reaction_to_id:
            return index

    # if not found
    return None


def handle(reaction, url, fb_credentials, firebase):
    if positive_reaction(reaction):
        fb.connect_and_store_url(url, fb_credentials, firebase)
    # printer.add_stored_reaction(url_cache)


def is_confirmation(reaction, url_cache_list, reaction_to_id):
    if not known_reaction(reaction):
        return None

    return get_index(url_cache_list, reaction_to_id)
