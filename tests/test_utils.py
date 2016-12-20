import pytest
import linkatos.utils as utils


# test message from bot
def test_from_bot():
    input_message = {
        'user': 'bot_id'
    }

    assert utils.from_bot(input_message, 'bot_id') is True


# test message contents
def test_has_text():
    input_message = {
        'text': 'sample text',
        'channel': 'channel'
    }

    assert utils.has_text(input_message) is True


def test_has_channel():
    input_message = {
        'channel': 'example'
    }

    assert utils.has_channel(input_message) is True
