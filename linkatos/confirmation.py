import linkatos.printer as printer


def update_confirmation_if_url(parsed_message, expecting_confirmation):
    if parsed_message['out'] is not None:
        if expecting_confirmation is False and
           parsed_message['type'] is 'url':
            expecting_confirmation = True

            url = parsed_message['out']
            printer.bot_says(channel, "Do you want me to store the link " +
                     url + " for you?")

    return (expecting_confirmation)


def process_confirmation_if_yn(parsed_message, expecting_confirmation):
    if expecting_confirmation is True and
        parsed_message['type'] is 'yn_answer':
        is_yes = out
        expecting_confirmation = False

        if is_yes is True:
            # store_url(link) # function not yet ready
            printer.bot_says(channel, url + " has been stored")

    return (expecting_confirmation)



