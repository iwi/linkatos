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


def handle(reaction, url, fb_credentials, firebase):
"""
Handles a reaction to a specific url. That is storing the url or ignoring it
depending on the reaction.
"""
    if positive_reaction(reaction):
        fb.connect_and_store_url(url, fb_credentials, firebase)
