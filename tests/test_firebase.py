import pytest
from . import firebase as fb


def test_to_data():
    url = 'https://foo.com'
    data = {'url': 'https://foo.com'}
    assert fb.to_data(url) == data
