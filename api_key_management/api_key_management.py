import os

import requests
from locker import Locker


class SlackLog:
    def __init__(self, slack_webhook):
        self.slack_webhook = slack_webhook

    def log(self, message):
        requests.post(
            url=self.slack_webhook,
            json={"text": f"```{message}```"},
            timeout=10
        )


if __name__ == '__main__':
    # Get the secret hook from Locker Secrets Manager
    client = Locker(
        access_key_id=os.getenv("YOUR_ACCESS_KEY_ID"),
        secret_access_key=os.getenv("YOUR_SECRET_ACCESS_KEY"),
    )
    webhook = client.get("SLACK_WEBHOOK")
    # Init the slack logger
    slack_logger = SlackLog(slack_webhook=webhook)
    slack_logger.log(message="Locker Secrets Manager")
