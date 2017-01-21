from . import parser
from . import printer
from . import firebase as fb
from . import reaction as react
from . import message
from . import cache as cch


def is_empty(events):
    """
    Checks if a batch of Slack events is `None` or has zero elements.
    """
    return ((events is None) or (len(events) == 0))


def is_usable(element, bot_id):
    """
    Checks if there is a new element(url) by verifying that is  not `None` and
    that it is not from the bot.
    The input is supposed to be a Slack event, but that's currently not
    verified.
    """
    return element is not None and is_not_from_bot(bot_id, element['user'])


def is_not_from_bot(bot_id, user_id):
    """
    Compares two bot ids and verifies that they're different.

    is this really necessary??
    """
    return not bot_id == user_id


def is_unfurled(event):
    """
    Checks if a Slack event comes from unfurling a url.

    Currently assumes that any such message can be identified by the fact that
    it contains a 'previous_message' field.
    """
    return 'previous_message' in event


def message_consumer(event, cache, slack_client, bot_id, fb_credentials,
                     firebase):
    """
    Consumes an event of type 'message' that contains a user.
    It looks inside the 'text' field for:
        + a url
        + @linkatos list
        + @linkatos purge <i>
       where <i> is the ith element of the cache
    """
    url = parser.parse_url_message(event)

    if is_usable(url, bot_id):
        return cch.add(url, cache, slack_client)

    if message.to_bot(event['text'], bot_id):
        list_request = parser.parse_list_request(event)
        purge_request = parser.parse_purge_request(event)

        if list_request is not None and list_request['type'] == 'list_request':
            cch.display(cache,
                        list_request['channel'],
                        slack_client)
            return cache

        if purge_request is not None and \
           purge_request['type'] == 'purge_request' and \
           not cch.is_empty(cache):
            cch.extract_url_by_index(cache,
                                     purge_request['index'] - 1)
            cch.display(cache,
                        purge_request['channel'],
                        slack_client)
            return cache

        return cache

    return cache


def reaction_added_consumer(event, cache, fb_credentials, firebase):
    """
    Consumes an event of type 'reaction_added' that respond to a cached url
    with either a :+1: or a :-1:
    """
    reaction = parser.parse_reaction_added(event)

    if react.is_known(reaction['reaction']):
        selected_url = cch.extract_url_by_id(cache,
                                             reaction['to_id'])
        react.handle(reaction['reaction'], selected_url['url'],
                     fb_credentials, firebase)
        return cache

    return cache

def event_consumer(cache, slack_client, bot_id, fb_credentials, firebase):
    """
    Consumes batches of slack events and runs the possible actions.

    Reads new batches of Slack events.
    Selects those events that need to be actioned. Currently they must be of
    type 'message' or of type 'reaction_added'
    """
    # Read slack events
    events = slack_client.rtm_read()

    if is_empty(events):
        return cache

    for event in events:
        if is_unfurled(event):
            return cache

        if event['type'] == 'message' and 'username' not in event:
            return message_consumer(event, cache, slack_client, bot_id,
                                    fb_credentials, firebase)

        if event['type'] == 'reaction_added' and len(cache) > 0:
            return reaction_added_consumer(event, cache, fb_credentials,
                                           firebase)
    return cache
