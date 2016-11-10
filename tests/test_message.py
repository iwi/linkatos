import pytest
import linkatos.message as message

def test_contains_a_https_url():
    expected = "https://example.org"

    assert message.contains_a_link("foo https://example.org") == expected
