import linkatos.message as message
import linkatos.utils


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
    output = {'out': None, 'channel' : None, 'type' : None})

    if is_empty(input_message):
        return (output)  # empty output

    for message in input_message:
        if from_bot(message, BOT_ID) or not has_text(message) or not
            has_channel(message):
            return (output)  # empty output

        output['channel'] = input_message['channel']

        text = input_message['text']
        output['out'] = extract_url(text)

        if output['out'] is not None:
            output['type'] = 'url'
            return (output)  # url output
        else:
            output['out'] = has_a_yes(text)

            if output['out'] is True:
                output['type'] = 'yn_answer'
                return (output)  # True y/n answer
            else:
                if has_a_no(text) is True:
                    output['type'] = 'yn_answer'
                    output['out'] = False
                    return (output)  # False y/n answer

    return (output)
