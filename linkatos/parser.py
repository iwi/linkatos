import linkatos.message as message
import linkatos.utils
import linkatos.utils as utils


def is_empty(message_list):
    return ((message_list is None) or (len(message_list) == 0))


def capture_reaction(sub_message):
    parsed['message'] = sub_message['reaction']
    parsed['channel'] = sub_message['item']['channel']
    parsed['item_ts'] = sub_message['item']['ts']
    parsed['type'] = 'reaction'
    parsed['user'] = sub_message['user']
    parsed['item_user'] = sub_message['item_user']
    return parsed


def capture_url(sub_message):
    parsed['channel'] = sub_message['channel']
    parsed['ts'] = sub_message['ts']
    parsed['type'] = 'url'
    parsed['user'] = sub_message['user']
    return parsed


def parse(input_message, BOT_ID):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless:
        1. someone posts a url starting with httpS?//
           in this case it returns the url and a out_type = 'url'
        2. someone adds a thumbsup or a thumbsdown
           in this case it returns the reaction and the type of outcome
    """
    print(input_message)  # print the list of outputs to get them on screen

    # default outcome
    parsed = {'message': None,
              'channel': None,
              'ts': None,
              'item_ts': None,
              'type': None,
              'user': None,
              'item_user': None}

    # if the message list is empty return an empty object
    if is_empty(input_message):
        return (parsed)

    for sub_message in input_message:
        if not utils.has_text(sub_message) or \
           not utils.has_channel(sub_message) or \
           utils.from_bot(sub_message, BOT_ID):
            return parsed  # empty output

        # if the message is a thumbsup reaction
        if sub_message['type'] == 'reaction_added' and \
           (sub_message['reaction'] == '+1' or sub_message['reaction'] == '-1'):
            parsed = capture_reaction(sub_message)
            return parsed

        # extract url from text if there is one
        text = sub_message['text']
        parsed['mesage'] = message.extract_url(text)

        # if a url was found return the relevant data
        if parsed['message'] is not None:
            parsed = capture_url(sub_message)
            return parsed  # url output

    return (parsed)
