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


def test_equal_ids():
    url_cache_list = [
        {'id': 'a'},
        {'id': 'b'},
        {'id': 'c'},
        {'id': 'd'},
    ]
    id_two = 'b'
    extracted = {'id': 'b'}
    assert react.extract_url_cache_by_id(url_cache_list, id_two) == extracted


def test_different_ids():
    url_cache_list = [
        {'id': 'a'},
        {'id': 'b'},
        {'id': 'c'},
        {'id': 'd'},
    ]
    id_two = 'e'
    assert react.extract_url_cache_by_id(url_cache_list, id_two) is None


def test_found_index():
    url_cache_list = [
        {'id': 'a'},
        {'id': 'b'},
        {'id': 'c'},
        {'id': 'd'},
    ]
    index = 2 - 1
    extracted = {'id': 'b'}
    assert react.extract_url_cache_by_index(url_cache_list, index) == extracted


def test_out_of_bounds_index():
    url_cache_list = [
        {'id': 'a'},
        {'id': 'b'},
        {'id': 'c'},
        {'id': 'd'},
    ]
    index = 5
    assert react.extract_url_cache_by_index(url_cache_list, index - 1) is None
