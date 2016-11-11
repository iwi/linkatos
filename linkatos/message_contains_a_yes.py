#! /bin/env python
import re

yes_re = re.compile("[Yy][eE].[sS].")

def message_contains_a_yes (message):
    """
    Returns a link if it matches the regex
    """
    answer = yes_re.search(message)
    if answer is not None:
        answer = answer.group(0).strip()

    return answer


