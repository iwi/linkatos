import pytest
from linkatos.message_contains_a_link import message_contains_a_link

def test_contains_a_https_url():
    expected = "https://example.org"

    assert message_contains_a_link("foo https://example.org") == expected
