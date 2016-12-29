from . import parser
from . import printer
from . import firebase as fb
from . import reaction as react


def is_empty(events):
    return ((events is None) or (len(events) == 0))


def is_url(url_cache):
    return url_cache is not None


def is_expected_reaction(index):
    return index is not None


def remove_url_from(url_cache_list, index):
    url_cache_list.pop(index)


def is_not_from_bot(bot_id, user_id):
    return not bot_id == user_id


def event_consumer(url_cache_list, slack_client, bot_id,
                   fb_credentials, firebase):
    # Read slack events
    events = slack_client.rtm_read()

    if is_empty(events):
        return url_cache_list

    for event in events:
        print('event: ', event)

        if event['type'] == 'message':
            new_url_cache = parser.parse_url_message(event)

            if is_url(new_url_cache) and is_not_from_bot(bot_id,
                                                         new_url_cache['user']):
                url_cache_list.append(new_url_cache)
                printer.ask_confirmation(new_url_cache, slack_client)

        print('url_cache_list: ', url_cache_list)

        if event['type'] == 'reaction_added' and len(url_cache_list) > 0:
            reaction = parser.parse_reaction_added(event)
            index = react.is_confirmation(reaction['reaction'], url_cache_list,
                                          reaction['to_id'])

            print('index: ', index)

            if is_expected_reaction(index):
                react.handle(reaction['reaction'], url_cache_list[index]['url'],
                             fb_credentials, firebase)
                remove_url_from(url_cache_list, index)

    return url_cache_list
