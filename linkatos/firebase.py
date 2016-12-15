import pyrebase


def initialise(api_key, project_name):
    config = {
      "apiKey": api_key,
      "authDomain": "{}.firebaseapp.com".format(project_name),
      "databaseURL": "https://{}.firebaseio.com".format(project_name),
      "storageBucket": "{}.appspot.com".format(project_name),
    }

    return pyrebase.initialize_app(config)

################################## user???????????????????
def authenticate_user(user, password, firebase):
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(user, password)
    return user


def get_db(firebase):
    return firebase.database()


def get_token(user):
    return user['idToken']


def store_url(url, db, token):
    return db.push(to_data(url), token)


def to_data(url):
    return {"url": url}



def xxxxxxxxxx(is_yes, url, user, password, firebase):
    # do nothing if it's unnecessary
    if not is_yes:
        return False

    db = get_db(firebase)
    user = authenticate_user(user, password, firebase)
    token = get_token(user, password, firebase)

    # creates token every time maybe worth doing it once every 30m as they
    # expire every hour

    db = firebase.database()
    data = {
        "url": url
    }

    db.child("users").push(data, user['idToken'])

    return False
