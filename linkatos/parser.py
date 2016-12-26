import message as message
import utils


def parse_url_message(event):
    url = message.extract_url(text)

    if url is None:
        empty_url_message = {
            'message': None,
            'channel': None,
            'id': None,
            'type': None,
            'user': None
        }

        return empty_url_message

    url_message = {
        'message': url,
        'channel': event['channel'],
        'id': event['ts'],
        'type': 'url',
        'user': event['user']
    }

    return url_message


def parse_reaction_added(event):
    reaction = {
        'reaction': event['reaction'],
        'channel': event['item']['channel'],
        'to_id': event['item']['ts'],
        'type': 'reaction',
        'user': event['user'],
        'to_user': event['item_user']
    }
    return parsed
