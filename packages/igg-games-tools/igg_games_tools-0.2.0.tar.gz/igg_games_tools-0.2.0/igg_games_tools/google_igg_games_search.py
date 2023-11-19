import re
from urllib.parse import quote

import bs4
import requests


def search_igg_games(name) -> list[str]:
    def func():
        res = requests.get(
            "https://p.jawide.repl.co/https://www.google.com/search?q={}".format(
                quote(name + " site:igg-games.com")
            )
        )

        soup = bs4.BeautifulSoup(res.text, "html.parser")

        results = soup.select(
            "#main > div > div.Gx5Zad.fP1Qef.xpd.EtOod.pkphOe > div.egMi0.kCrYT a"
        )
        for result in results:
            url = result["href"]
            urls = re.findall(r"(https://igg-games.com/.*.-free-download.html)", url)
            if len(urls) > 0:
                yield urls[0]

    return list(func())
