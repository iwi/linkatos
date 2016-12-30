import pytest
from linkatos import message


# test url detection
def test_basic_url_detection_of_https():
    expected = "https://example.org"
    text = "foo <https://example.org>"
    assert message.extract_url(text) == expected


def test_hash_in_url():
    expected = "https://foo.org#bar"
    text = "<https://foo.org#bar>"
    assert message.extract_url(text) == expected


def test_plus_in_url():
    expected = "http://foo.org/foo+bar"
    text = "<http://foo.org/foo+bar>"
    assert message.extract_url(text) == expected


def test_equal_in_url():
    expected = "http://example.org?q=foo"
    text = "<http://example.org?q=foo>"
    assert message.extract_url(text) == expected


def test_qmark_in_url():
    expected = "http://example.org?"
    text = "<http://example.org?>"
    assert message.extract_url(text) == expected


def test_and_in_url():
    expected = "http://example.org?foo=1&bar=2"
    text = "<http://example.org?foo=1&bar=2>"
    assert message.extract_url(text) == expected


def test_hyphen_in_url():
    expected = "https://this-is-a-test.org"
    text = "<https://this-is-a-test.org>"
    assert message.extract_url(text) == expected


def test_underscore_in_url():
    expected = "https://this_website.org"
    text = "<https://this_website.org>"
    assert message.extract_url(text) == expected


def test_detection_of_http_in_the_middle():
    expected = "http://example.com"
    text = "foo <http://example.com> bar"
    assert message.extract_url(text) == expected


def test_message_does_not_have_a_url():
    text = "foo <htts://no_url_example.org>"
    assert message.extract_url(text) is None


def test_to_bot():
    text = '<@bot_id>'
    bot_id = 'bot_id'
    assert message.to_bot(text, bot_id) is True


def test_not_to_bot():
    text = '<@not_bot_id>'
    bot_id = 'bot_id'
    assert message.to_bot(text, bot_id) is False


def test_is_list():
    text = 'list'
    assert message.is_list_request(text) is True


def test_is_not_list():
    text = 'lOst'
    assert message.is_list_request(text) is False
