from . import parser
from . import printer
from . import firebase as fb
from . import reaction as react


def is_empty(events):
    return ((events is None) or (len(events) == 0))


def is_url(url_cache):
    return url_cache is not None

def event_consumer(expecting_url, url_cache, slack_client,
                   fb_credentials, firebase):

    # Read slack events
    events = slack_client.rtm_read()

    if is_empty(events):
        return (expecting_url, url_cache)

    for event in events:
        print(event)
        print('expecting_url: ', expecting_url)

        if expecting_url and event['type'] == 'message':
            url_cache = parser.parse_url_message(event)

            if url_cache is not None:
                printer.ask_confirmation(url_cache, slack_client)
                expecting_url = False

        if not expecting_url and event['type'] == 'reaction_added':
            reaction = parser.parse_reaction_added(event)

            if react.is_confirmation(reaction['reaction'],
                                     url_cache['id'],
                                     reaction['to_id']):
                react.handle(reaction['reaction'], url_cache['url'],
                             fb_credentials, firebase)
                expecting_url = True

    return (expecting_url, url_cache)
