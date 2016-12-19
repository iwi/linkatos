import time
import linkatos.parser as parser
import linkatos.confirmation as confirmation
import linkatos.printer as printer
import linkatos.utils as utils
import linkatos.firebase as fb


def keep_wanted_urls(expecting_confirmation, url, slack_client, BOT_ID,
                     fb_credentials, firebase):
    READ_WEBSOCKET_DELAY = 1  # 1 second delay between reading from firehose

    # parse the messages. Get a dictionary with
    # {'message': <url or reaction (:+1: or :-1:)>,
    # 'channel': <channel where the message was posted>,
    # 'ts': <timestamp - used as identifier>,
    # 'item_ts': <for reactions, timestamp of the item>,
    # 'type': <'url', 'reaction'>,
    # 'user': <user id>,
    # 'item_user': <for reactions the user that posted the item>}
    parsed_message = parser.parse(slack_client.rtm_read(), BOT_ID)

    print(parsed_message)
    print(expecting_confirmation)

    if utils.is_fresh_url(expecting_confirmation, parsed_message['type']):
        url = parsed_message['message']

    print(url)

    printer.ask_confirmation(expecting_confirmation, parsed_message, slack_client)

    # update expecting_confirmation
    # when it's a url
    expecting_confirmation = confirmation.update_if_url(parsed_message,
                                                        expecting_confirmation)

    # check if there is an answer
    (expecting_confirmation, confirmed) = confirmation.evaluate(parsed_message,
                                                                expecting_confirmation)

    # printer.notify_confirmation(expecting_confirmation, is_yes)

    # Store url
    if confirmed:
        fb.connect_and_store_url(url, fb_credentials, firebase)
        # confirmed = False

    time.sleep(READ_WEBSOCKET_DELAY)

    return (expecting_confirmation, url)
