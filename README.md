# Slackbot to capture urls

## Summary

This project intends to:
  - Create a Slackbot that detects any url posted on a channel where
    the bot has been invited
  - Capture the url in a database


## Running the bot

Currently the bot can only be run with:
  ```
  $ python linkatos.py
  ```

It's necessary to add the following environment variables:

### API token

```
export SLACK_BOT_TOKEN='API token name'
```

### Bot ID

```
export BOT_ID='bot ID'
```

## Tests





## Tools

The initial choices of tools are:
  - Python to create the bot
  - Beep Boop to host and run the bot
  - Firebase to store the links

## Sources

The slack bot was based on:
> A simple Python-powered starter Slack bot
> [the tutorial](https://www.fullstackpython.com/blog/build-first-slack-bot-python.html)

