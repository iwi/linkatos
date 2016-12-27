import pytest
import linkatos.activities as message


def test_None_event():
    event = None
    assert is_empty(event) is True


def test_len_zero_event():
    event = []
    assert is_empty(event) is True


def test_message_is_url():
    message = {'type': 'url'}
    assert is_url(message) is True
