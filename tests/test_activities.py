import pytest
import linkatos.activities as activities


def test_none_event():
    event = None
    assert activities.is_empty(event) is True


def test_len_zero_event():
    event = []
    assert activities.is_empty(event) is True


def test_message_is_url():
    message = {'type': 'url'}
    assert activities.is_url(message) is True
