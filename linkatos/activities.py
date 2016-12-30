from . import parser
from . import printer
from . import firebase as fb
from . import reaction as react
from . import message


def is_empty(events):
    return ((events is None) or (len(events) == 0))


def is_url(url_cache):
    return url_cache is not None


def is_not_from_bot(bot_id, user_id):
    return not bot_id == user_id


def is_unfurled(event):
    return 'previous_message' in event


def event_consumer(url_cache_list, slack_client, bot_id,
                   fb_credentials, firebase):
    # Read slack events
    events = slack_client.rtm_read()

    if is_empty(events):
        return url_cache_list

    for event in events:
        if is_unfurled(event):
            return url_cache_list

        if event['type'] == 'message' and not 'username' in event:
            new_url_cache = parser.parse_url_message(event)

            if is_url(new_url_cache) and is_not_from_bot(bot_id,
                                                         new_url_cache['user']):
                url_cache_list.append(new_url_cache)
                printer.ask_confirmation(new_url_cache, slack_client)

            if message.to_bot(event['text'], bot_id):
                list_request = parser.parse_list_request(event)
                purge_request = parser.parse_purge_request(event)

                if 'type' in list_request and list_request['type'] == 'list_request':
                    printer.list_cached_urls(url_cache_list,
                                             list_request['channel'],
                                             slack_client)

                if purge_request['type'] == 'purge_request':
                    remove_url_from(url_cache_list, purge_request['index'] - 1)

        if event['type'] == 'reaction_added' and len(url_cache_list) > 0:
            reaction = parser.parse_reaction_added(event)

            if react.is_known(reaction['reaction']):
                selected_url_cache = react.extract_url_cache(url_cache_list,
                react.handle(reaction['reaction'], selected_url_cache['url'],
                             fb_credentials, firebase)

    return url_cache_list
