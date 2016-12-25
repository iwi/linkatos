import linkatos.message as message
import linkatos.utils
import linkatos.utils as utils


def is_empty(message_list):
    return ((message_list is None) or (len(message_list) == 0))


def capture_reaction(message):
    parsed = {
        'message': message['reaction'],
        'channel': message['item']['channel'],
        'item_ts': message['item']['ts'],
        'type': 'reaction',
        'user': message['user'],
        'item_user': message['item_user']
    }
    return parsed


def capture_url(message, url):
    parsed = {
        'message': url,
        'channel': message['channel'],
        'ts': message['ts'],
        'type': 'url',
        'user': message['user']
    }
    return parsed


def parse(input_message):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless:
        1. someone posts a url starting with httpS?//
           in this case it returns the url and a out_type = 'url'
        2. someone adds a thumbsup or a thumbsdown
           in this case it returns the reaction and the type of outcome
    """
    print('input_message:', input_message)  # print the list of outputs to get them on screen

    # default outcome
    parsed = {
        'message': None,
        'channel': None,
        'ts': None,
        'item_ts': None,
        'type': None,
        'user': None,
        'item_user': None
    }

    # if the message list is empty return an empty object
    if is_empty(input_message):
        return (parsed)

    for message in input_message:
        print('message:', message)

        # capture a reaction if the message is a thumbsup/down reaction
        if utils.has_reaction_keys(message) and \
           message['type'] == 'reaction_added' and \
           (message['reaction'] == '+1' or message['reaction'] == '-1'):
            parsed = capture_reaction(message)
            return parsed

        # extract url from text if there is text and it has a url
        if utils.has_text_keys(message):
            text = message['text']
            url = message.extract_url(text)

            # if a url was found return the relevant data
            if url is not None:
                parsed = capture_url(message, url)
                return parsed  # url output

    return parsed


def parse_url_message(event):
    url = message.extract_url(text)

    if url is None:
        empty_url_message = {
            'message': None,
            'channel': None,
            'id': None,
            'type': None,
            'user': None
        }

        return empty_url_message

    url_message = {
        'message': url,
        'channel': event['channel'],
        'id': event['ts'],
        'type': 'url',
        'user': event['user']
    }

    return (url_message)

def parse_reaction_added(event):
    reaction = {
        'reaction': event['reaction'],
        'channel': event['item']['channel'],
        'to_id': event['item']['ts'],
        'type': 'reaction',
        'user': event['user'],
        'to_user': event['item_user']
    }
    return parsed



