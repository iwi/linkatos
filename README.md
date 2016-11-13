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

To run the tests execute:

```sh
make build test
```

This has been tested with Docker (1.12.1) and GNU Make (4.1).
These versions are the lowest that have been tested but lower versions might be
acceptable as well.


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

See [LICENCE](https://github.com/iwi/linkatos/blob/master/LICENCE)
