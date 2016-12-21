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


def test_has_text_keys():
    message = {
        'text': 'foo',
        'channel': 'sample_channel',
        'ts': 1234.1234,
        'user': 'sample_user'
    }
    assert utils.has_text_keys(message) is True


def test_doesnt_have_text_key():
    message = {
        'channel': 'sample_channel',
        'ts': 1234.1234,
        'user': 'sample_user'
    }
    assert utils.has_text_keys(message) is False


def test_doesnt_have_channel_key():
    message = {
        'text': 'foo',
        'ts': 1234.1234,
        'user': 'sample_user'
    }
    assert utils.has_text_keys(message) is False


def test_doesnt_have_ts_key():
    message = {
        'text': 'foo',
        'channel': 'sample_channel',
        'user': 'sample_user'
    }
    assert utils.has_text_keys(message) is False


def test_doesnt_have_user_key():
    message = {
        'text': 'foo',
        'channel': 'sample_channel',
        'ts': 1234.1234
    }
    assert utils.has_text_keys(message) is False


def test_has_reaction_keys():
    message = {
        'reaction': '+1',
        'item': 'example_item',
        'item': {'ts': 1234.1234,
                 'channel': 'example_channel'
                 },
        'user': 'example_user',
        'item_user': 'example_item_user'
    }
    assert utils.has_reaction_keys(message) is True
