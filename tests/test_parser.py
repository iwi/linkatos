import pytest
import linkatos.parser as parser


def test_parse_reaction_added():
    event = {
        'reaction': '+1',
        'channel': 'example_channel',
        'item': {
            'channel': 'example_channel',
            'ts': 1234.1234
        },
        'user': 'example_user',
        'item_user': 'example_item_user'
    }
    reaction = {
        'reaction': '+1',
        'channel': 'example_channel',
        'to_id': 1234.1234,
        'type': 'reaction',
        'user': 'example_user',
        'to_user': 'example_item_user'
    }
    assert parser.parse_reaction_added(event) == reaction


def test_parse_url():
    event = {
        'text': '<http://foo.bar>',
        'channel': 'example_channel',
        'ts': 1234.1234,
        'user': 'example_user'
    }
    parsed_url = {
        'url': 'http://foo.bar',
        'channel': 'example_channel',
        'id': 1234.1234,
        'type': 'url',
        'user': 'example_user'
    }
    assert parser.parse_url_message(event) == parsed_url


def test_empty_message():
    event = {
        'text': 'not a url',
        'channel': 'example_channel',
        'ts': 1234.1234,
        'user': 'example_user'
    }
    assert parser.parse_url_message(event) is None
