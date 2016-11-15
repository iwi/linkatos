import re
import os

link_re = re.compile("https?://\S+(\s|$)")
yes_re = re.compile("(\s|^)(Yes|YES|yes)(\s|[,.]|$)")
no_re = re.compile("(\s|^)(No|NO|no)(\s|[,.]|$)")
BOT_ID = os.environ.get("BOT_ID")


def extract_url(message):
    """
    Returns the first url in a message. If there aren't any returns None
    """

    answer = link_re.search(message)

    if answer is not None:
        answer = answer.group(0).strip()

    return answer


def has_a_yes(message):
    """
    Returns True if it matches the yes regex
    """
    return yes_re.search(message) is not None


def has_a_no(message):
    """
    Returns True if it matches the no regex
    """
    return no_re.search(message) is not None

def parse(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless
        someone posts a website link starting with httpS?//, a yes or a no
    """
    # default outcome

    output_list = slack_rtm_output
    print(output_list)  # print the list of outputs to get them on screen

    if (output_list is None) or (len(output_list) == 0):
        return (None, None, None)

    for output in output_list:
        if output is None or 'text' not in output or output['user'] == BOT_ID:
            print("output none or text not there or user bot")
            return (None, None, None)

        text = output['text']
        out_type = None
        out = None
        url = extract_url(text)

        if url is not None:
            out_type = 'url'
            out = url
        else:
            is_yes = has_a_yes(text)
            if is_yes is True:
                out_type = 'yn_answer'
                out = is_yes
            else:
                if has_a_no(text) is True:
                    out_type = 'yn_answer'
                    out = False

        if 'channel' in output:
            channel = output['channel']

    return (out, channel, out_type)


