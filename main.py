import os
import requests  # noqa We are just importing this to prove the dependency installed correctly
import time


def main():
    API_KEY = os.environ["INPUT_BITLYTOKEN"]
    LONG_URL = os.environ["INPUT_LONGURL"]

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + API_KEY}
    data = {"long_url": LONG_URL}
    API_ENDPOINT = "https://api-ssl.bitly.com/v4/shorten"

    # Request for bitly shortened link
    r = None
    r = requests.post(url=API_ENDPOINT, headers=headers, json=data)
    while True:
        time.sleep(1)
        if r is not None:
            break
    if(r.status_code == 200 or r.status_code == 201):
        shortened_link = r.json()["link"]
    else:
        shortened_link = ""

    print(f"::set-output name=shortURL::{shortened_link}")

    output = "Hello world"
    print(f"::set-output name=myOutput::{output}")


if __name__ == "__main__":
    main()
