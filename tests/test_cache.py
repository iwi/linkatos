import pytest
from linkatos import cache as cch


def test_equal_ids():
    cache = [
        {'id': 'a'},
        {'id': 'b'},
        {'id': 'c'},
        {'id': 'd'},
    ]
    id_two = 'b'
    extracted = {'id': 'b'}
    assert cch.extract_url_by_id(cache, id_two) == extracted


def test_different_ids():
    url_cache_list = [
        {'id': 'a'},
        {'id': 'b'},
        {'id': 'c'},
        {'id': 'd'},
    ]
    id_two = 'e'
    assert cch.extract_url_by_id(url_cache_list, id_two) is None


def test_found_index():
    cache = [
        {'id': 'a'},
        {'id': 'b'},
        {'id': 'c'},
        {'id': 'd'},
    ]
    index = 2 - 1
    extracted = {'id': 'b'}
    assert cch.extract_url_by_index(cache, index) == extracted


def test_out_of_bounds_index():
    cache = [
        {'id': 'a'},
        {'id': 'b'},
        {'id': 'c'},
        {'id': 'd'},
    ]
    index = 5
    assert cch.extract_url_by_index(cache, index - 1) is None
