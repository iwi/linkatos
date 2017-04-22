# Slackbot to capture urls

## Summary

This slackbot:

  - Detects any url posted on a channel where the bot is invited, and
  - Captures the detected urls into a database


## Features

When the bot is invited to a channel it automatically caches the urls that are
posted.

Use a :+1: reaction to the message where the url was posted the bot stores the
url into a Firebase database.

Use a :-1: reaction to the message where the url was posted the bot ignores
that url.

Use `@linkatos list` to ask linkatos to list all cached urls that have not yet
been stored or ignored.

Use `@linkatos purge <i>` to ask linkatos to remove the ith element from the
cache as stated when running `@linkatos list`.

## Setting up the credentials

The bot needs credentials to connect to the Slack team and to connect to the
Firebase database. The credentials need to be stored in a file named `.env` on
the root _linkatos_ directory.

The `.env` file must contain:

```
FB_API_KEY=xxxx
FB_USER=xxxx
FB_PASS=xxxx
BOT_ID=xxxx
SLACK_BOT_TOKEN=xxxx
```
_Note that tokens, username and password must not include quotes or extra
spaces._

The `FB_API_KEY` can be found on the _Project settings_ on your project's
Firebase web UI.

The `FB_USER` and `FB_PASS` can be added to the _Authentication_ settings
within the project's Firebase web UI.

The `BOT_ID` and the `SLACK_BOT_TOKEN` can be obtained from the Slack web
client... (expand)

## Running the bot

To run the bot in isolation use the Dockerised version:

First build the bot:

```sh
make build
```

Then install and run

```sh
make install
```

To see the logs execute:

```sh
make logs
```

And, to stop the process and remove the Docker container:

```sh
make clean
```


If you run it outside Docker, first install the dependencies:

```sh
pip install -r requirements.txt
```

Then

```sh
SLACK_BOT_TOKEN=apitoken BOT_ID=botid FB_API_KEY=firebase_api_key FB_USER=firebase_user FB_PASS="firebase_password" ./linkatos.py
```


## Tests

To run the tests execute:

```sh
make build test
```


## Lint

To run the linter:

```sh
make build lint
```


## Tools

The initial choices of tools are:
  - Python 3 to create the bot
  - [Firebase](https://firebase.google.com) to store the links
  - _[Beep Boop](https://beepboophq.com) to host and run the bot_


## Sources

The slack bot was initially based on:
> A simple Python-powered starter Slack bot
> [the tutorial](https://www.fullstackpython.com/blog/build-first-slack-bot-python.html)


## Licence

Linkatos is licensed under the MIT License. See [LICENCE](https://github.com/iwi/linkatos/blob/master/LICENCE)
