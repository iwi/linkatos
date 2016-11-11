import pytest
from linkatos.message_contains_a_link import message_contains_a_link

def test_contains_a_https_url():
    expected = "https://example.org"

    assert message_contains_a_link("foo https://example.org") == expected


def test_contains_a_http_url():
    expected = "http://example.com"

    assert message_contains_a_link("foo http://example.com bar") == expected

def test_is_not_a_url():

    assert message_contains_a_link("foo htts://example.org") == None


