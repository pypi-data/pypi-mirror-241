import re
from urllib.parse import quote

import bs4
import requests


def create_download_link1(url):
    res = requests.post("http://127.0.0.1:8191/v1", json={
        "cmd": "request.get",
        "url": url
    })
    if res.status_code != 200:
        return create_download_link(url)

    text = res.json()["solution"]["response"]

    soup = bs4.BeautifulSoup(text, "html.parser")

    form = soup.select_one("form")
    inputs = form.select("input[name]")
    url = form["action"] + "?" + "&".join(["=".join([inp["name"], quote(inp["value"])]) for inp in inputs])
    return url


def create_download_link(url):
    res = requests.post("http://127.0.0.1:8191/v1", json={
        "cmd": "request.get",
        "url": url,
    })
    if res.status_code != 200:
        return create_download_link(url)

    text = res.json()["solution"]["response"]

    url = re.findall("'btndownload','([^']*)'", text)[0]
    return url


def parse_real_download_link(url):
    res = requests.post("http://127.0.0.1:8191/v1", json={
        "cmd": "request.get",
        "url": url
    })
    if res.status_code != 200:
        return parse_real_download_link(url)

    text = res.json()["solution"]["response"]

    soup = bs4.BeautifulSoup(text, "html.parser")
    a = soup.select_one("body > div.text > a")
    url = a["href"]
    return url
