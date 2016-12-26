import time
import linkatos.parser as parser
import linkatos.printer as printer
import linkatos.firebase as fb
import linkatos.reaction as react


def is_empty(events):
    return ((events is None) or (len(events) == 0))


def is_url(url_message):
    return url_message['type'] == 'url'


def event_consumer(expecting_url, expecting_reaction, parsed_url_message,
                   slack_client, fb_credentials, firebase):
    READ_WEBSOCKET_DELAY = 1  # 1 second delay between reading from firehose

    # Read slack events
    events = slack_client.rtm_read()

    if is_empty(events):
        return (expecting_url, expecting_reaction, parsed_url_message)

    for event in events:
        print(event)
        print('expecting_url: ', expecting_url)
        print('expecting_reaction: ', expecting_reaction)
        if 'type' in event:
            if expecting_url and event['type'] == 'message':
                parsed_url_message = parser.parse_url_message(event)

                if is_url(parsed_url_message):
                    printer.ask_confirmation(parsed_url_message, slack_client)
                    expecting_url = False
                    expecting_reaction = True

            if expecting_reaction and event['type'] == 'reaction_added':
                reaction = parser.parse_reaction_added(event)

                if react.is_confirmation(reaction['reaction'],
                                         parsed_url_message['id'],
                                         reaction['to_id']):
                    react.handle(reaction['reaction'], parsed_url_message['url'],
                                 fb_credentials, firebase)
                    expecting_reaction = False
                    expecting_url = True
        time.sleep(READ_WEBSOCKET_DELAY)



    time.sleep(READ_WEBSOCKET_DELAY)

    return (expecting_url, expecting_reaction, parsed_url_message)
