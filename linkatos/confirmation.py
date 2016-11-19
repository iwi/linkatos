import linkatos.printer as printer
from .utils import is_fresh_url


def update_confirmation_if_url(parsed_message, expecting_confirmation):
    if is_fresh_url(expecting_confirmation, parsed_message['type']):
        expecting_confirmation = True

    return (expecting_confirmation)


def process_confirmation_if_yn(parsed_message, expecting_confirmation):
    is_yes = None
    if expecting_confirmation is True and parsed_message['type'] is 'yn_answer':
        is_yes = parsed_message['out']
        expecting_confirmation = False

    return (expecting_confirmation, is_yes)
