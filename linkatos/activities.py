import time
import linkatos.parser as parser
import linkatos.confirmation as confirmation
import linkatos.printer as printer
import linkatos.utils as utils
import linkatos.firebase as fb


def keep_wanted_urls(expecting_confirmation, parsed_url_message, slack_client,
                     BOT_ID, fb_credentials, firebase):
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

    print('parsed_message:', parsed_message)
    print('expecting_confirmation:', expecting_confirmation)

    if utils.is_fresh_url(expecting_confirmation, parsed_message['type']):
        parsed_url_message = parsed_message
        expecting_confirmation = True
        printer.ask_confirmation(parsed_message, slack_client)

    print('parsed_url_message:', parsed_url_message)


    # check if there is an answer
    if parsed_url_message:
        item_ts = parsed_url_message['ts']
    else:
        item_ts = None

    (expecting_confirmation, confirmed) = confirmation.evaluate(expecting_confirmation,
                                                                parsed_message,
                                                                item_ts)

    print('confirmed:', confirmed)

    # printer.notify_confirmation(expecting_confirmation, is_yes)

    # Store url
    if confirmed:
        url =  parsed_url_message['message']
        fb.connect_and_store_url(url, fb_credentials, firebase)
        # confirmed = False

    time.sleep(READ_WEBSOCKET_DELAY)

    return (expecting_confirmation, parsed_url_message)
