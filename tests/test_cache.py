import pytest
from linkatos import cache as cch
from linkatos.cache import Cache

def test_init_cache():
    assert isinstance(Cache([]), Cache)


def test_is_empty():
    c = Cache([])
    assert c.is_empty()


def test_is_not_empty():
    c = Cache([1])
    assert not c.is_empty()


def test_add():
    element = {'id': 'a'}
    c = Cache([])
    c.add(element)
    assert c.find('a') == element


def test_find():
    element = {'id': 'a'}
    c = Cache([element])
    assert c.find('a') == element


def test_find_nothing():
    element = {'id': 'a'}
    c = Cache([element])
    assert c.find('b') is None


def test_find_by_index():
    element = {'id': 'a'}
    c = Cache([element])
    assert c.find_by_index(0) == element


def test_find_by_index_nothing():
    element = {'id': 'a'}
    c = Cache([element])
    assert c.find_by_index(1) is None


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
