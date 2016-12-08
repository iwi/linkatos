import pyrebase


def initialise(FB_API_KEY):
    config = {
        "apiKey": FB_API_KEY,
        "authDomain": "coses-acbe6.firebaseapp.com",
        "databaseURL": "https://coses-acbe6.firebaseio.com",
        "storageBucket": "coses-acbe6.appspot.com"}

    return pyrebase.initialize_app(config)


def store_url(is_yes, url, FB_USER, FB_PASS, firebase):
    # do nothing if it's unnecessary
    if not is_yes:
        return False

    # creates token every time maybe worth doing it once every 30m as they
    # expire every hour
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(FB_USER, FB_PASS)

    db = firebase.database()
    data = {
        "url": url
    }

    db.child("users").push(data, user['idToken'])

    return False
