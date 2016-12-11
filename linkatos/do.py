import linkatos.parser as parser
import linkatos.confirmation as confirmation
import linkatos.printer as printer
import linkatos.utils as utils


def keep_wanted_urls(expecting_confirmation, url):
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
   expecting_confirmation = confirmation.update_if_url(
        parsed_message,
        expecting_confirmation
    )

    # check if there is an answer
    (expecting_confirmation, is_yes) = confirmation.process_if_yn(
        parsed_message,
        expecting_confirmation
    )

    # printer.notify_confirmation(expecting_confirmation, is_yes)

    # Store url
    is_yes = fb.store_url(is_yes, url, FB_USER, FB_PASS, firebase)

    time.sleep(READ_WEBSOCKET_DELAY)

    return (expecting_confirmation, url)
