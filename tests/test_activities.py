import pytest
from linkatos import activities


def test_none_event():
    event = None
    assert activities.is_empty(event) is True


def test_len_zero_event():
    event = []
    assert activities.is_empty(event) is True


def test_unusable_element():
    element = None
    bot_id = "bot_id"
    assert activities.is_usable(element, bot_id) is False

