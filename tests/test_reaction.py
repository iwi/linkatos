import pytest
import linkatos.reaction as react

def test_positive_reaction():
    reaction = '+1'
    assert react.positive_reaction(reaction) is True


def test_not_positive_reaction():
    reaction = '-1'
    assert react.positive_reaction(reaction) is False


def test_known_reaction_neg():
    reaction = '-1'
    assert react.known_reaction(reaction) is True


def test_known_reaction_pos():
    reaction = '+1'
    assert react.known_reaction(reaction) is True


def test_unknown_reaction():
    reaction = 'worried'
    assert react.known_reaction(reaction) is False


def test_equal_ids():
    id_one = 'id'
    id_two = 'id'
    assert react.reacting_to_url(id_one, id_two) is True


def test_different_ids():
    id_one = 'id1'
    id_two = 'id2'
    assert react.reacting_to_url(id_one, id_two) is False


def test_confirmation():
    reaction = '+1'
    url_message_id = 'id'
    reaction_to_id = 'id'
    assert react.is_confirmation(reaction, url_message_id, reaction_to_id) is True
