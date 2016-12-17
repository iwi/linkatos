import pyrebase


def initialise(api_key, project_name):
    config = {
      "apiKey": api_key,
      "authDomain": "{}.firebaseapp.com".format(project_name),
      "databaseURL": "https://{}.firebaseio.com".format(project_name),
      "storageBucket": "{}.appspot.com".format(project_name),
    }

    return pyrebase.initialize_app(config)


def authenticate(credentials, auth):
    user = auth.sign_in_with_email_and_password(credentials['username'],
                                                credentials['password'])
    return user


def get_token(credentials, firebase):
    user = authenticate(credentials,
                        firebase.auth())
    return user['idToken']


def to_data(url):
    return {"url": url}


def store_url(url, db, token):
    return db.push(to_data(url), token)


def urls_db(firebase):
    return firebase.database().child('urls')


def connect_and_store_url(url, credentials, firebase):
    # the function should only be called if we need to store the url
    token = get_token(credentials, firebase)
    db = urls_db(firebase)
    store_url(url, db, token)
