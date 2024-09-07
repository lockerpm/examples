import os

from flask import Flask, jsonify
from locker import Locker
from locker.error import ResourceNotFoundError

app = Flask(__name__)


@app.route('/configuration')
def configuration():
    client = Locker(
        access_key_id=os.getenv("YOUR_ACCESS_KEY_ID"),
        secret_access_key=os.getenv("YOUR_SECRET_ACCESS_KEY"),
    )
    try:
        config_data = {
            "smtp": {
                "from": client.get("SMTP_FROM"),
                "from_name": client.get("SMTP_FROM_NAME"),
                "host": client.get("SMTP_HOST"),
                "port": client.get("SMTP_PORT"),
                "username": client.get("SMTP_USERNAME"),
                "password": client.get("SMTP_PASSWORD")
            },
            "sso": {
                "client_id": client.get("SSO_CLIENT_ID"),
                "redirect_url": client.get("SSO_REDIRECT_URL"),
            }
        }
    except ResourceNotFoundError:
        config_data = {
            "smtp": None,
            "sso": None,
        }
    return jsonify(config_data)
