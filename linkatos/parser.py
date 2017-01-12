from . import message


def parse_url_message(event):
    url = message.extract_url(event['text'])

    if url is None:
        return None

    url_cache = {
        'url': url,
        'channel': event['channel'],
        'id': event['ts'],
        'type': 'url',
        'user': event['user']
    }

    return url_cache


def parse_reaction_added(event):
    reaction = {
        'reaction': event['reaction'],
        'channel': event['item']['channel'],
        'to_id': event['item']['ts'],
        'type': 'reaction',
        'user': event['user'],
        'to_user': event['item_user']
    }

    return reaction


def parse_list_request(event):
    if not message.is_list_request(event['text']):
        return None

    list_request = {
        'channel': event['channel'],
        'type': 'list_request'
    }

    return list_request


def parse_purge_request(event):
    index = message.purge_request(event['text'])
    if index is None:
        return None

    purge_request = {
        'index': index,
        'type': 'purge_request',
        'channel': event['channel']
    }

    return purge_request
