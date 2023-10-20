import os
import requests
from mastodon import Mastodon

token = os.environ.get("TOKEN")

mastodon = Mastodon(
    access_token=f"{token}",
    api_base_url="https://botsin.space"
)

def random_fact():
    fact = requests.get("https://catfact.ninja/fact?max_length=280").json()
    return fact["fact"]


def main():
    fact = random_fact()
    mastodon.status_post(status=fact)


if __name__ == "__main__":
    main()