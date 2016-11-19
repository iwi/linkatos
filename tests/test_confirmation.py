import pytest
import linkatos.confirmation as confirmation


def confirmation_on_if_url():

    expecting_confirmation = False
    parsed_m = {'out' : 'http://ex.org', 'channel' : 'ch', 'type' : 'url'}

    assert confirmation.update_confirmation_if_url(parsed_m, expecting_confirmation) is True


# to do test process_confirmation_if_yn(parsed_message, expecting_confirmation)

