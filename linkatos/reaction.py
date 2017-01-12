from . import firebase as fb


def positive_reaction(reaction):
    return reaction == '+1'


def is_known(reaction):
    return reaction in ['+1', '-1']


def extract_url_cache_by_id(url_cache_list, reaction_to_id):
    for index in range(0, len(url_cache_list)):
        if url_cache_list[index]['id'] == reaction_to_id:
            url_cache = url_cache_list[index]
            url_cache_list.pop(index)
            return url_cache

    # if not found
    return None


def extract_url_cache_by_index(url_cache_list, index):
    if (index > len(url_cache_list) - 1) or (index < 0):
        return None

    url_cache = url_cache_list[index]
    url_cache_list.pop(index)
    return url_cache


def handle(reaction, url, fb_credentials, firebase):
    if positive_reaction(reaction):
        fb.connect_and_store_url(url, fb_credentials, firebase)
