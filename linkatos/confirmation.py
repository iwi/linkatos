import linkatos.printer as printer
from .utils import is_fresh_url


def update_confirmation_if_url(parsed_message, expecting_confirmation):
    if is_fresh_url(expecting_confirmation, parsed_message['type']):
        expecting_confirmation = True

    return (expecting_confirmation)


def process_confirmation_if_yn(parsed_message, expecting_confirmation):
    if expecting_confirmation is False or parsed_message['type'] is not 'yn_answer':
        is_yes = False
        return (expecting_confirmation, is_yes)

    is_yes = parsed_message['out']  # True if 'yes', False if 'no'
    expecting_confirmation = False

    return (expecting_confirmation, is_yes)
