import re

link_re = re.compile("https?://\S+(\s|$)")
yes_re = re.compile("(/b|^)(Yes|YES|yes)(/b|,|/.|$)")

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
