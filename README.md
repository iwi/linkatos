# Slackbot to capture urls

## Summary

This project intends to:
  - Create a Slackbot that detects any url posted on a channel where
    the bot has been invited
  - Capture the url in a database


## Running the bot

Currently the bot can only be run with:
  ```sh
  SLACK_BOT_TOKEN=apitoken BOT_ID=botid ./linkatos.py
  ```

## Tests

Lorem ipsum


## Tools

The initial choices of tools are:
  - Python 3 to create the bot
  - [Beep Boop](https://beepboophq.com) to host and run the bot
  - [Firebase](https://firebase.google.com) to store the links


## Sources

The slack bot was based on:
> A simple Python-powered starter Slack bot
> [the tutorial](https://www.fullstackpython.com/blog/build-first-slack-bot-python.html)

## Licence

See [LICENCE](https://github.com/iwi/linkatos/blob/master/LICENSE)
