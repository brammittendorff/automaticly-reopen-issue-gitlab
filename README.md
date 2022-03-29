# Automaticly reopen Service Desk issues on Gitlab

This application will make sure you can automatily reopen Service Desk issues on Gitlab.

## Requirements

- python
- pip
- requirements.txt

## Installation

Please make sure you test the webhook on <https://webhook.site> to see what value BOT_USERNAME should have in your case.

## Environment variables

Create a `.env` file with the following contents:

```
SECRET_KEY="somesecretkeyfromdjango"
BOT_USERNAME="support-bot"
GITLAB_ACCESS_TOKEN="your-specialaccestokengitlab"
GITLAB_API_URL="https://gitlab.com/api/v4/projects/support%2Fbot"
```

- Note: remember if you are using this url to make sure you will use instead of a `/` the character `%2F`.
  
- Note: if you want to set the x-gitlab-token to make sure unauthorized people can not use this webhook you can use the env variable: `GITLAB_X_TOKEN`

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