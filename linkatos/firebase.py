import pyrebase


def initialise(api_key, project_name):
    config = {
      "apiKey": api_key,
      "authDomain": "{}.firebaseapp.com".format(project_name),
      "databaseURL": "https://{}.firebaseio.com".format(project_name),
      "storageBucket": "{}.appspot.com".format(project_name),
    }

    return pyrebase.initialize_app(config)


def authenticate_user(username, password, auth):
    user = auth.sign_in_with_email_and_password(username, password)
    return user


def get_db(firebase):
    return firebase.database()


def get_token(user):
    return user['idToken']


def store_url(url, db, token):
    return db.child("users").push(to_data(url), token)


def get_auth(firebase):
    return firebase.auth()


def to_data(url):
    return {"url": url}


def connect_to_fb_and_store_url(url, username, password, firebase):
    # the function should only be called if we need to store the url
    auth = get_auth(firebase)
    user = authenticate_user(username, password, auth)
    token = get_token(user)
    data = to_data(url)
    db = get_db(firebase)
    store_url(url, db, token)
