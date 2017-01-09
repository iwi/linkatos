import pyrebase


def initialise(api_key, project_name):
"""
Connects to the Firebase project.
"""
    config = {
      "apiKey": api_key,
      "authDomain": "{}.firebaseapp.com".format(project_name),
      "databaseURL": "https://{}.firebaseio.com".format(project_name),
      "storageBucket": "{}.appspot.com".format(project_name),
    }

    return pyrebase.initialize_app(config)


def authenticate(credentials, auth):
"""
Authenticates to the Firebase project.
"""
    user = auth.sign_in_with_email_and_password(credentials['username'],
                                                credentials['password'])
    return user


def get_token(credentials, firebase):
"""
Gets a new token for the Firebase project.
"""
    user = authenticate(credentials,
                        firebase.auth())
    return user['idToken']


def to_data(url):
"""
Converts a string with a url to a jason object that contains a url.
"""
    return {"url": url}


def store_url(url, db, token):
"""
Stores a url json object to the Firebase project.
"""
    return db.push(to_data(url), token)


def urls_db(firebase):
"""
Specifies the 'urls' database within db.
"""
    return firebase.database().child('urls')


def connect_and_store_url(url, credentials, firebase):
"""
Connects and stores a url to the Firebase project database in 'urls'.
"""
    # the function should only be called if we need to store the url
    token = get_token(credentials, firebase)
    db = urls_db(firebase)
    store_url(url, db, token)
