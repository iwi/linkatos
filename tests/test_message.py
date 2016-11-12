import pytest
import linkatos.message as message


# test link detection

def test_message_has_a_https_url():
    expected = "https://example.org"

    assert message.extract_url("foo https://example.org") == expected


def test_message_has_a_http_url():
    expected = "http://example.com"

    assert message.extract_url("foo http://example.com bar") == expected


def test_message_does_not_have_a_url():
    assert message.extract_url("foo htts://example.org") is None


# test yes detection

def test_message_with_yes_between_spaces():
    assert message.has_a_yes("foo yes bar") is True


def test_message_with_yes_only():
    assert message.has_a_yes("yes") is True


def test_message_without_a_yes():
    assert message.has_a_yes("foo yea bar") is False


def test_message_with_end_of_word_yes():
    assert message.has_a_yes("bayes") is False


def test_message_with_beginning_of_word_yes():
    assert message.has_a_yes("yesares") is False


def test_message_with_beginning_of_word_Yes():
    assert message.has_a_yes("Yesterday") is False


def test_message_with_middle_of_word_yes():
    assert message.has_a_yes("reyesado") is False
