import pytest
import linkatos.confirmation as confirmation


def test_no_confirmation_with_url():
    expecting_confirmation = False
    parsed_m = {'out': 'http://ex.org', 'channel': 'ch', 'type': 'url'}

    assert confirmation.update_if_url(parsed_m,
                                                   expecting_confirmation) is True


# to do test process_confirmation_if_yn(parsed_message, expecting_confirmation)

def test_confirmation_with_url():
    expecting_confirmation = True
    parsed_m = {'out': 'http://ex.org', 'channel': 'ch', 'type': 'url'}

    assert confirmation.update_if_url(parsed_m,
                                                   expecting_confirmation) is True


def test_confirmation_without_url():
    expecting_confirmation = True
    parsed_m = {'out': None, 'channel': 'ch', 'type': None}

    assert confirmation.update_if_url(parsed_m,
                                                expecting_confirmation) is True


def test_no_confirmation_without_url():
    expecting_confirmation = False
    parsed_m = {'out': None, 'channel': 'ch', 'type': None}

    assert confirmation.update_if_url(parsed_m,
                                               expecting_confirmation) is False
