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


def get_cat_pic():
    url = "https://api.thecatapi.com/v1/images/search"
    cats = requests.request("GET", url).json()
    cat_pic = cats[0]["url"]
    img_data = requests.get(cat_pic).content
    with open("cat_pic.jpg", "wb") as handler:
        handler.write(img_data)
    return mastodon.media_post("cat_pic.jpg")


def main():
    fact = random_fact()
    media = get_cat_pic()
    mastodon.status_post(status=fact, media_ids=media)


if __name__ == "__main__":
    main()
