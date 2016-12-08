import pyrebase


def initialise(api_key, project_name):
    config = {
      "apiKey": api_key,
      "authDomain": "{}.firebaseapp.com".format(project_name),
      "databaseURL": "https://{}.firebaseio.com".format(project_name),
      "storageBucket": "{}.appspot.com".format(project_name),
    }

    return pyrebase.initialize_app(config)


def store_url(is_yes, url, user, password, firebase):
    # do nothing if it's unnecessary
    if not is_yes:
        return False

    # creates token every time maybe worth doing it once every 30m as they
    # expire every hour
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(user, password)

    db = firebase.database()
    data = {
        "url": url
    }

    db.child("users").push(data, user['idToken'])

    return False
