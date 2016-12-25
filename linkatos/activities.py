import time
import parser
import confirmation
import printer
import utils
import firebase as fb


def is_empty(events):
    return ((events is None) or (len(events) == 0))


def handle(reaction, url, fb_credentials, firebase):
    if reaction['reaction'] == '+1':
        fb.connect_and_store_url(url, fb_credentials, firebase)

    # printer.add_stored_reaction(parsed_url_message)


def event_consumer(expecting_url, expecting_reaction, parsed_url_message,
                   slack_client, fb_credentials, firebase):

    READ_WEBSOCKET_DELAY = 1  # 1 second delay between reading from firehose

    events = slack_client.rtm_read()

    if is_empty(events):
        return (expecting_url, expecting_reaction, parsed_url_message)

    for event in events:
        if 'type' in event:
            if event['type'] == 'message' and expecting_url:
                parsed_url_message = parser.parse_url_message(event)

                if is_url(parsed_url_message):
                    printer.ask_confirmation(parsed_url_message, slack_client)
                    expecting_url = False
                    expecting_reaction = True

            if event['type'] == 'reaction_added' and expecting_reaction:
                reaction = parser.parse_reaction_added(event)

                if is_confirmation(reaction['reaction'],
                                   parsed_url_message['id']
                                   reaction['to_id']):
                    handle(reaction, parsed_url_message['url'],
                           fb_credentials, firebase)
                    expecting_reaction = False
                    expecting_url = True

    time.sleep(READ_WEBSOCKET_DELAY)

    return (expecting_url, expecting_reaction, parsed_url_message)
