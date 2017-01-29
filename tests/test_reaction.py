import pytest
from linkatos import reaction as react


def test_positive_reaction():
    reaction = '+1'
    assert react.positive_reaction(reaction) is True


def test_not_positive_reaction():
    reaction = '-1'
    assert react.positive_reaction(reaction) is False


def test_known_reaction_neg():
    reaction = '-1'
    assert react.is_known(reaction) is True


def test_known_reaction_pos():
    reaction = '+1'
    assert react.is_known(reaction) is True


def test_unknown_reaction():
    reaction = 'worried'
    assert react.is_known(reaction) is False
