import pyrebase


def store_url(is_yes, url, FB_API_KEY, FB_USER, FB_PASS, firebase):
    # do nothing if it's unnecessary
    if not is_yes:
        return is_yes

    # creates token every time maybe worth doing it once every 30m as they
    # expire every hour
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(FB_USER, FB_PASS)

    db = firebase.database()
    data = {
        "url": url
    }

    db.child("users").push(data, user['idToken'])

    is_yes = False

    return is_yes
