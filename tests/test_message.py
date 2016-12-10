import pytest
import linkatos.message as message


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
    expected = "https://wikipedia.org/title=foo"
    text = "<https://wikipedia.org/title=foo>"
    assert message.extract_url(text) == expected


def test_qmark_in_url():
    expected = "http://wik.org/index.php?title"
    text = "<http://wik.org/index.php?title>"
    assert message.extract_url(text) == expected


def test_and_in_url():
    expected = "https://foo.org/alpha&beta"
    text = "<https://foo.org/alpha&beta>"
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
