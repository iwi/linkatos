import linkatos.message as message
import linkatos.utils
import linkatos.utils as utils


def is_empty(message_list):
    return ((message_list is None) or (len(message_list) == 0))


def parse(input_message, BOT_ID):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless:
        1. someone posts a url starting with httpS?//
           in this case it returns the url and a out_type = 'url'
        2. a yes or a no after a url
           in this case it returns True for a yes, False for a no
        The function also extracts the name of the channel
    """
    print(input_message)  # print the list of outputs to get them on screen

    # default outcome
    parsed = {'out': None, 'channel': None, 'type': None}

    if is_empty(input_message):
        return (parsed)  # empty output

    for sub_message in input_message:
        if not utils.has_text(sub_message) or \
           not utils.has_channel(sub_message) or \
           utils.from_bot(sub_message, BOT_ID):
            return (parsed)  # empty output

        parsed['channel'] = sub_message['channel']

        text = sub_message['text']
        parsed['out'] = message.extract_url(text)

        if parsed['out'] is not None:
            parsed['type'] = 'url'
            return (parsed)  # url output
        else:
            parsed['out'] = utils.has_a_yes(text)

            if parsed['out'] is True:
                parsed['type'] = 'yn_answer'
                return (parsed)  # True y/n answer
            else:
                if utils.has_a_no(text) is True:
                    parsed['type'] = 'yn_answer'
                    parsed['out'] = False
                    return (parsed)  # False y/n answer

    return (parsed)
