import json
import requests
import logging
from requests.structures import CaseInsensitiveDict
from django.conf import settings
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse('ping')


@csrf_exempt
def webhook(request):
    logger.info("Triggered webhook")
    x_gitlab_token = request.headers['x-gitlab-token']
    if x_gitlab_token:
        if settings.GITLAB_X_TOKEN != x_gitlab_token:
            logger.warning(
                "Wrong x-gitlab-token!")
            raise PermissionDenied()
    if request.body:
        json_body = json.loads(request.body)
        if json_body and json_body['user'] and json_body['user']['username']:
            if json_body['user']['username'] == settings.BOT_USERNAME:
                logger.info("Bot username is correct: {username}".format(
                    username=json_body['user']['username']))
                # Do put request to reopen issue because user replies
                url = "{gitlab_url}/issues/{issue}?state_event=reopen".format(
                    issue=json_body['issue']['iid'], gitlab_url=settings.GITLAB_API_URL)
                headers = CaseInsensitiveDict()
                headers["Content-Type"] = "application/x-www-form-urlencoded"
                headers["PRIVATE-TOKEN"] = settings.GITLAB_ACCESS_TOKEN

                resp = requests.put(url, headers=headers)
                if resp.status_code == 200:
                    logger.info("Reopend the issue: {iid}".format(
                        iid=json_body['issue']['iid']))
                else:
                    logger.warning("Possibly the gitlab access token is wrong, or you got a malformed gitlab url!")

    return HttpResponse(request)
