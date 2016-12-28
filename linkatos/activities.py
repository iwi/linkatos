from . import parser
from . import printer
from . import firebase as fb
from . import reaction as react


def is_empty(events):
    return ((events is None) or (len(events) == 0))


def is_url(url_cache):
    return url_cache is not None


def is_reaction(index):
    return index is not None


def event_consumer(expecting_url, url_cache_list, slack_client,
                   fb_credentials, firebase):
    # Read slack events
    events = slack_client.rtm_read()

    if is_empty(events):
        return (expecting_url, url_cache)

    for event in events:
        print(event)

        if expecting_url and event['type'] == 'message':
            new_url_cache = parser.parse_url_message(event)
            url_cache_list.append(new_url_cache)

            if is_url(new_url_cache):
                printer.ask_confirmation(new_url_cache, slack_client)

        if event['type'] == 'reaction_added':
            reaction = parser.parse_reaction_added(event)
            index = react.is_confirmation(reaction['reaction'], url_cache_list,
                                          reaction['to_id']):

            if is_reaction(index):
                react.handle(reaction['reaction'], url_cache_list[index]['url'],
                             fb_credentials, firebase)
                remove_url_from(url_cache_list)

    return (expecting_url, url_cache)
