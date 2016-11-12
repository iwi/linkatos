#! /bin/env python

import pytest
import linkatos.message as message


# test link detection

def test_contains_a_https_url():
    expected = "https://example.org"

    assert message.contains_a_link("foo https://example.org") == expected


def test_contains_a_http_url():
    expected = "http://example.com"

    assert message.contains_a_link("foo http://example.com bar") == expected


def test_is_not_a_url():

    assert message.contains_a_link("foo htts://example.org") is None

# test yes detection

def test_contains_a_yes():
    expected = "yes"

    assert message.contains_a_yes("foo yes bar") == expected


def test_is_not_a_yes():

    assert message.contains_a_yes("foo yea bar") is None
