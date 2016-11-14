import pytest
import linkatos.message as message

# test link detection

def test_message_has_a_https_url():
    expected = "https://example.org"

    assert message.extract_url("foo https://example.org") == expected


def test_message_has_a_http_url():
    expected = "http://example.com"

    assert message.extract_url("foo http://example.com bar") == expected


def test_message_does_not_have_a_url():
    assert message.extract_url("foo htts://example.org") is None


# test yes detection

def test_message_with_yes_between_spaces():
    assert message.has_a_yes("foo yes bar") is True


def test_message_with_yes_only():
    assert message.has_a_yes("yes") is True


def test_message_without_a_yes():
    assert message.has_a_yes("foo yea bar") is False


def test_message_with_end_of_word_yes():
    assert message.has_a_yes("bayes") is False


def test_message_with_beginning_of_word_yes():
    assert message.has_a_yes("yesares") is False


def test_message_with_beginning_of_word_Yes():
    assert message.has_a_yes("Yesterday") is False


def test_message_with_middle_of_word_yes():
    assert message.has_a_yes("reyesado") is False


# test no detection

def test_message_has_no_inbetween_spaces():
    assert message.has_a_no("foo no bar") is True


# test message parsing

def test_ignore_linkatos_message():
    output_example = [
        {'user_profile': {'image_72':'image.png',
                          'avatar_hash': 'hash',
                          'real_name': '',
                          'first_name': None,
                          'name': 'name'},
         'team': 'team',
         'bot_id': 'bot_id',
         'user': 'U2YJMEX2P',  # is it wrong to have this on a test?
         'channel': 'channel',
         'text': 'http://example.org',
         'type': 'message',
         'user_team': 'user_team'}
    ]

    assert (None, None, None) == parse_output(output_example)


def test_is_of_url_type():
    output_example = [
        {'user_profile': {'image_72':'image.png',
                          'avatar_hash': 'hash',
                          'real_name': '',
                          'first_name': None,
                          'name': 'name'},
         'team': 'team',
         'bot_id': 'bot_id',
         'user': 'user',
         'channel': 'channel',
         'text': 'http://example.org',
         'type': 'message',
         'user_team': 'user_team'}
    ]

    assert ("http://example.org", 'channel', 'url') == parse_output(output_example)


def test_is_of_ynanswer_type():
    output_example = [
        {'user_profile': {'image_72':'image.png',
                          'avatar_hash': 'hash',
                          'real_name': '',
                          'first_name': None,
                          'name': 'name'},
         'team': 'team',
         'bot_id': 'bot_id',
         'user': 'user',
         'channel': 'channel',
         'text': 'yes',
         'type': 'message',
         'user_team': 'user_team'}
    ]

    assert ("yes", 'channel', 'yn_answer') == parse_output(output_example)


