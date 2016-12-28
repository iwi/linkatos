from . import firebase as fb


def positive_reaction(reaction):
    return reaction == '+1'


def known_reaction(reaction):
    return reaction in ['+1', '-1']


def reacting_to_url(url_message_id, reaction_to_id):
    return url_message_id == reaction_to_id


def handle(reaction, url, fb_credentials, firebase):
    if positive_reaction(reaction):
        fb.connect_and_store_url(url, fb_credentials, firebase)
    # printer.add_stored_reaction(url_cache)


def is_confirmation(reaction, url_message_id, reaction_to_id):
    return reacting_to_url(url_message_id, reaction_to_id) and known_reaction(reaction)
