"""
Line notification function.
"""
import os

import requests
from dotenv import load_dotenv

load_dotenv()


def notify(message: str) -> None:
    """Must set the following environment variables: LINE_NOTIFY_URL LINE_NOTIFY_SECRET_TOKEN at .env file."""
    url = os.environ["LINE_NOTIFY_URL"]
    token = os.environ["LINE_NOTIFY_SECRET_TOKEN"]
    headers = {"Authorization": "Bearer " + token}
    requests.post(url, headers=headers, params={"message": message})


if __name__ == "__main__":
    notify("Sample message")
