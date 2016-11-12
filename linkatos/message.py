#! /bin/env python

import re

link_re = re.compile("https?://\S+(\s|$)")

def contains_a_link(message):
    """
    Returns a link if it matches the regex
    """

    answer = link_re.search(message)

    if answer is not None:
        answer = answer.group(0).strip()

    return answer


yes_re = re.compile("(Yes|YES|yes)")

def contains_a_yes(message):
    """
    Returns a yes if it matches the regex
    """
    answer = yes_re.search(message)
    if answer is not None:
        answer = answer.group(0).strip()

    return answer
