import pytest
import linkatos.utils as utils


# test yes detection
def test_message_with_yes_between_spaces():
    assert utils.has_a_yes("foo yes bar") is True


def test_message_with_yes_only():
    assert utils.has_a_yes("yes") is True


def test_message_without_a_yes():
    assert utils.has_a_yes("foo yea bar") is False


def test_message_with_end_of_word_yes():
    assert utils.has_a_yes("bayes") is False


def test_message_with_beginning_of_word_yes():
    assert utils.has_a_yes("yesares") is False


def test_message_with_beginning_of_word_Yes():
    assert utils.has_a_yes("Yesterday") is False


def test_message_with_middle_of_word_yes():
    assert utils.has_a_yes("reyesado") is False


# test no detection
def test_message_has_no_inbetween_spaces():
    assert utils.has_a_no("foo no bar") is True


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
