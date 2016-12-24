import linkatos.message as message
import linkatos.utils
import linkatos.utils as utils


def is_empty(message_list):
    return ((message_list is None) or (len(message_list) == 0))


def capture_reaction(sub_message):
    parsed = {
        'message': sub_message['reaction'],
        'channel': sub_message['item']['channel'],
        'item_ts': sub_message['item']['ts'],
        'type': 'reaction',
        'user': sub_message['user'],
        'item_user': sub_message['item_user']
    }
    return parsed


def capture_url(sub_message, url):
    parsed = {
        'message': url,
        'channel': sub_message['channel'],
        'ts': sub_message['ts'],
        'type': 'url',
        'user': sub_message['user']
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

    for sub_message in input_message:
        print('sub_message:', sub_message)

        # capture a reaction if the message is a thumbsup/down reaction
        if utils.has_reaction_keys(sub_message) and \
           sub_message['type'] == 'reaction_added' and \
           (sub_message['reaction'] == '+1' or sub_message['reaction'] == '-1'):
            parsed = capture_reaction(sub_message)
            return parsed

        # extract url from text if there is text and it has a url
        if utils.has_text_keys(sub_message):
            text = sub_message['text']
            url = message.extract_url(text)

            # if a url was found return the relevant data
            if url is not None:
                parsed = capture_url(sub_message, url)
                return parsed  # url output

    return parsed
