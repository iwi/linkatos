import linkatos.printer as printer
from .utils import is_fresh_url


def update_if_url(parsed_message, expecting_confirmation):
    if is_fresh_url(expecting_confirmation, parsed_message['type']):
        expecting_confirmation = True

    return (expecting_confirmation)


def evaluate_reaction(reaction):
    return reaction == '+1'


def known_reaction(reaction):
    return reaction in ['+1', '-1']


def evaluate(parsed_message, url_message_id):
    if parsed_message['type'] != 'reaction':
        return None

    reaction = parsed_message['message']
    reaction_message_id = parsed_message['item_ts']

    if not known_reaction(reaction) or reaction_message_id != url_message_id:
        return None

    return evaluate_reaction(reaction)
