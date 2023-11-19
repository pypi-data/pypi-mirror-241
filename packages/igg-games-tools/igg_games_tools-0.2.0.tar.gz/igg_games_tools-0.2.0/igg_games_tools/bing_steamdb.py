import bs4
import requests
import fake_useragent
from urllib.parse import quote


def related_games(name) -> list[str]:
    response = requests.get(
        f"https://cn.bing.com/search?q={quote(name)}%20site:steamdb.info",
        headers={
            "user-agent": fake_useragent.FakeUserAgent().random
        }
    )
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    results = soup.select("#b_results > li > h2 > a")
    return [r.text.split("·")[0].strip() for r in results]
