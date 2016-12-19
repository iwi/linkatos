import linkatos.printer as printer
from .utils import is_fresh_url


def update_if_url(parsed_message, expecting_confirmation):
    if is_fresh_url(expecting_confirmation, parsed_message['type']):
        expecting_confirmation = True

    return (expecting_confirmation)


def evaluate(parsed_message, expecting_confirmation):
    # returns (@expecting_confirmation: boolean, @confirmation: boolean)
    if expecting_confirmation is False or parsed_message['type'] is not 'reaction':
        return (False, False)

    if parsed_message['message'] == '+1':
        return (False, True)

    if parsed_message['message'] == '-1':
        return (False, False)

    # when we're expecting a confirmation and it's not a thumbs up or a thumbs
    # down, we keep waiting
    return (expecting_confirmation, False)
