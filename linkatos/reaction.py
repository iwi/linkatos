def handle(reaction, url, fb_credentials, firebase):
    if reaction['reaction'] == '+1':
        fb.connect_and_store_url(url, fb_credentials, firebase)

    # printer.add_stored_reaction(parsed_url_message)

def is_confirmation(reaction, url_message_id, reaction_to_id):
    if reacting_to_url(url_message_id, reaction_to_id) and
       known_reaction(reaction):
        return True


