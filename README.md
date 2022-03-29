# Automaticly reopen Service Desk issues on Gitlab

This application will make sure you can automatily reopen Service Desk issues on Gitlab.

## Requirements

- python
- pip
- requirements.txt

## Installation

## Environment variables

Create a `.env` file with the following contents:

```
BOT_USERNAME="support-bot"
GITLAB_ACCESS_TOKEN="your-specialaccestokengitlab"
GITLAB_API_URL="https://gitlab.com/api/v4/projects/support%2Fbot"
```

Note: remember if you are using this url to make sure you will use instead of a `/` the character `%2F`.

## Installing the packages

```
pip install -r requirements.txt
```

## Usage

You can deploy this project directly to Heroku or run it locally with:

```
./manage.py runserver
```

And if you run it locally you can use a service like ngrok / localtunnel to test the webhooks.