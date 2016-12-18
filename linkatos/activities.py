import time
import linkatos.parser as parser
import linkatos.confirmation as confirmation
import linkatos.printer as printer
import linkatos.utils as utils
import linkatos.firebase as fb


def keep_wanted_urls(expecting_confirmation, url, slack_client, BOT_ID,
                     fb_credentials, firebase):
    READ_WEBSOCKET_DELAY = 1  # 1 second delay between reading from firehose

    # parse the messages. Get a dictionary with @out, @channel,
    # @out_type
    parsed_message = parser.parse(slack_client.rtm_read(), BOT_ID)

    print(parsed_message)
    print(expecting_confirmation)

    if utils.is_fresh_url(expecting_confirmation, parsed_message['type']):
        url = parsed_message['out']

    print(url)

    printer.ask_confirmation(expecting_confirmation, parsed_message, slack_client)

    # update expecting_confirmation
    # when it's a url
    expecting_confirmation = confirmation.update_if_url(parsed_message,
                                                        expecting_confirmation)

    # check if there is an answer
    (expecting_confirmation, is_yes) = confirmation.process_if_yn(parsed_message,
                                                                  expecting_confirmation)

    # printer.notify_confirmation(expecting_confirmation, is_yes)

    # Store url
    if is_yes:
        fb.connect_and_store_url(url, fb_credentials, firebase)
        is_yes = False

    time.sleep(READ_WEBSOCKET_DELAY)

    return (expecting_confirmation, url)