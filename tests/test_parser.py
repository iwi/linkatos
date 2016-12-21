import pytest
import linkatos.parser as parser


# test message parsing
def test_ignore_linkatos_message():
    message = [{
        'user': 'bot_id',
        'channel': 'channel',
        'text': 'http://example.org'
    }]

    parsed = {'message': None,
              'channel': None,
              'ts': None,
              'item_ts': None,
              'type': None,
              'user': None,
              'item_user': None}


    assert parser.parse(message, 'bot_id') == parsed


def test_capture_reaction():
    message = {
        'reaction': '+1',
        'channel': 'example_channel',
        'item': {
            'channel': 'example_channel',
            'ts': 1234.1234
        },
        'user': 'example_user',
        'item_user': 'example_item_user'
    }

    reaction= {
        'message': '+1',
        'channel': 'example_channel',
        'item_ts': 1234.1234,
        'type': 'reaction',
        'user': 'example_user',
        'item_user': 'example_item_user'
    }

    assert parser.capture_reaction(message) == reaction


def test_capture_url():
    message = {
        'channel': 'example_channel',
        'ts': 1234.1234,
        'user': 'example_user',
    }

    url = 'http://foo.bar'

    parsed_url = {
        'message': 'http://foo.bar',
        'channel': 'example_channel',
        'ts': 1234.1234,
        'type': 'url',
        'user': 'example_user',
    }

    assert parser.capture_url(message, url) == parsed_url
