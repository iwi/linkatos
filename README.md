# Slackbot to capture urls

## Summary

This project intends to:
  - Create a Slackbot that detects any url posted on a channel where
    the bot has been invited
  - Capture the url in a database


## Running the bot

To run the bot in isolation use the Dockerised version:

First build the bot:

```sh
make build
```

Then

```sh
make install LINKATOS_SECRET=slacktoken LINKATOS_ID=botid
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
SLACK_BOT_TOKEN=apitoken BOT_ID=botid ./linkatos.py
```


## Tests

To run the tests execute:

```sh
make build test
```


## Tools

The initial choices of tools are:
  - Python 3 to create the bot
  - [Beep Boop](https://beepboophq.com) to host and run the bot
  - [Firebase](https://firebase.google.com) to store the links


## Sources

The slack bot was initially based on:
> A simple Python-powered starter Slack bot
> [the tutorial](https://www.fullstackpython.com/blog/build-first-slack-bot-python.html)

## Licence

Linkatos is licensed under the MIT License. See [LICENCE](https://github.com/iwi/linkatos/blob/master/LICENCE)
