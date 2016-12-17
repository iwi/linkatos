import pyrebase


def initialise(api_key, project_name):
    config = {
      "apiKey": api_key,
      "authDomain": "{}.firebaseapp.com".format(project_name),
      "databaseURL": "https://{}.firebaseio.com".format(project_name),
      "storageBucket": "{}.appspot.com".format(project_name),
    }

    return pyrebase.initialize_app(config)


def authenticate(username, password, auth):
    user = auth.sign_in_with_email_and_password(username, password)
    return user


def get_token(username, password, firebase):
    user = authenticate(username, password, firebase.auth())
    return user['idToken']


def to_data(url):
    return {"url": url}


def store_url(url, db, token):
    return db.child("users").push(to_data(url), token)


def connect_and_store_url(url, username, password, firebase):
    # the function should only be called if we need to store the url
    token = get_token(username, password, firebase)
    db = firebase.database()
    store_url(url, db, token)
