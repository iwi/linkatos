#! /bin/env python
import re

link_re = re.compile("https?://\S+(\s|$)")

def message_contains_a_link (message):
    """
    Returns a link if it matches the regex
    """
    answer = link_re.search(message)
    if answer is not None:
        answer = answer.group(0).strip()

    return answer

