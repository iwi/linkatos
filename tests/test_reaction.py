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
    assert react.known_reaction(reaction) is True


def test_known_reaction_pos():
    reaction = '+1'
    assert react.known_reaction(reaction) is True


def test_unknown_reaction():
    reaction = 'worried'
    assert react.known_reaction(reaction) is False


def test_equal_ids():
    url_cache_list = [
        {'id': 'a'},
        {'id': 'b'},
        {'id': 'c'},
        {'id': 'd'},
    ]
    id_two = 'b'
    assert react.get_index(url_cache_list, id_two) is 1


def test_different_ids():
    url_cache_list = [
        {'id': 'a'},
        {'id': 'b'},
        {'id': 'c'},
        {'id': 'd'},
    ]
    id_two = 'e'
    assert react.get_index(url_cache_list, id_two) is None


def test_is_expected_reaction():
    index = 1
    reaction = '+1'
    assert react.is_expected_reaction(index, reaction) is True
