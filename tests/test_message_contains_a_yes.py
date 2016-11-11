import pytest
from linkatos.message_contains_a_yes import message_contains_a_yes

def test_contains_a_yes():
    expected = "yes"

    assert message_contains_a_yes("foo yes bar") == expected
    assert message_contains_a_yes("foo yea bar") != expected

