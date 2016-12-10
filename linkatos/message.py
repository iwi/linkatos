import re

link_re = re.compile("(?:\s|^)<(https?://[\w./?+]+)>(?:\s|$)")


def extract_url(message):
    """
    Returns the first url in a message. If there aren't any returns None
    """
    answer = link_re.search(message)

    if answer is not None:
        answer = answer.group(1).strip()

    return answer
