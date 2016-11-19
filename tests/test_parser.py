import pytest
import linkatos.parser as parser


# test message parsing
def test_ignore_linkatos_message():
    input_example = [{
        'user': 'bot_id',
        'channel': 'channel',
        'text': 'http://example.org'
    }]

    output = {'out': None, 'channel': None, 'type': None}

    assert parser.parse(input_example, 'bot_id') == output


def test_is_of_url_type():
    input_example = [{
         'channel': 'channel',
         'text': 'http://example.org',
         'user': 'user'
    }]

    output = {'out': 'http://example.org', 'channel': 'channel', 'type': 'url'}

    assert parser.parse(input_example, 'bot_id') == output


def test_is_of_ynanswer_type_yes():
    input_example = [{
         'channel': 'channel',
         'text': 'yes',
         'user': 'user'
    }]

    output = {'out': True, 'channel': 'channel', 'type': 'yn_answer'}

    assert parser.parse(input_example, 'bot_id') == output


def test_is_of_ynanswer_type_no():
    input_example = [{
         'channel': 'channel',
         'text': 'No',
         'user': 'user'
    }]

    output = {'out': False, 'channel': 'channel', 'type': 'yn_answer'}

    assert parser.parse(input_example, 'bot_id') == output


def test_channelin_channelout():
    input_example = [{
         'channel': 'channel_in',
         'text': 'yes',
         'user': 'user'
    }]

    output = {'out': True, 'channel': 'channel_in', 'type': 'yn_answer'}

    assert parser.parse(input_example, 'bot_id') == output
