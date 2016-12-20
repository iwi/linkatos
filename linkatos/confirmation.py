import linkatos.printer as printer
from .utils import is_fresh_url


def update_if_url(parsed_message, expecting_confirmation):
    if is_fresh_url(expecting_confirmation, parsed_message['type']):
        expecting_confirmation = True

    return (expecting_confirmation)


def evaluate(expecting_confirmation, parsed_message, item_ts):
    # returns (@expecting_confirmation: boolean, @confirmation: boolean)
    print('1', expecting_confirmation)
    print('2', parsed_message['type'])
    if 'item_ts' in parsed_message: print('3', parsed_message['item_ts'] == item_ts)
    if expecting_confirmation is False or \
       parsed_message['type'] is not 'reaction' or \
       parsed_message['item_ts'] != item_ts:
        print('stopppppppped!')
        return (expecting_confirmation, False)

    print('the parsed reaction is:', parsed_message['message'])

    if parsed_message['message'] == '+1':
        return (False, True)

    if parsed_message['message'] == '-1':
        return (False, False)

    # when we're expecting a confirmation and it's not a thumbs up or a thumbs
    # down, we keep waiting
    print('went through!!!')
    return (expecting_confirmation, False)
