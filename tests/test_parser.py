import pytest
import linkatos.parser as parser

# test message parsing

def test_ignore_linkatos_message():
    output_example = [{
        'bot_id': 'bot_id',
        'channel': 'channel',
        'text': 'http://example.org'
    }]


    output = {'out': None, 'channel' : None, 'type' : None})

    assert parser.parse(message, 'bot_id') is output

def test_is_of_url_type():
    output_example = [{
         'channel': 'channel',
         'text': 'http://example.org',
    }]

    output = {'out': 'http://example.org', 'channel' : 'channel', 'type' :
        'url'})

    assert parser.parse(message, 'bot_id') is output


def test_is_of_ynanswer_type_yes():
    output_example = [{
         'channel': 'channel',
         'text': 'yes',
    }]

    output = {'out': True, 'channel' : 'channel', 'type' :
        'yn_answer'})

    assert parser.parse(message, 'bot_id') is output


def test_is_of_ynanswer_type_no():
    output_example = [{
         'channel': 'channel',
         'text': 'No',
    }]

    output = {'out': False, 'channel' : 'channel', 'type' :
        'yn_answer'})

    assert parser.parse(message, 'bot_id') is output


def test_channelin_channelout():
    output_example = [{
         'channel': 'channel_in',
         'text': 'yes',
    }]

    output = {'out': True, 'channel' : 'channel_in', 'type' :
        'yn_answer'})

    assert parser.parse(message, 'bot_id') is output
