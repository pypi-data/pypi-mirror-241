import re

import requests


def list_all_download_url(url: str) -> list[tuple[str, str]]:
    text = requests.get(url).text
    links = re.findall(r'>Link (.*):<.*\n?<a href="(.*)" target=', text)
    assert len(links) > 1, 'links not found'
    return links


def parse_bluemedia_url(url: str):
    def decode(code: str) -> str:
        result = ''
        i = len(code) / 0x2 - 0x5
        while i >= 0x0:
            result += code[int(i)]
            i = i - 0x2
        i = len(code) / 0x2 + 0x4
        while i < len(code):
            result += code[int(i)]
            i = i + 0x2
        return result

    url = url.replace(' ', '+')
    text = requests.get(url).text
    codes = re.findall(r'Goroi_n_Create_Button\("(.*)"\);', text)
    assert len(codes) == 1, 'codes not found'
    url = 'https://p.jawide.repl.co/http://bluemediafiles.com/get-url.php?url={}'.format(decode(codes[0]))
    return url.replace(' ', '+')


def pack_megaup_url1(url):
    def encode(d1, d2):
        url_da_encrypt = ""
        for i in range(len(d1) // 4 - 1, -1, -1):
            url_da_encrypt += d1[i]
        for i in range(len(d1) // 4 * 3 - 1, len(d1) // 4 * 2 - 1, -1):
            url_da_encrypt += d1[i]
        for i in range((len(d2) - 3) // 2 + 2, 2, -1):
            url_da_encrypt += d2[i]
        return url_da_encrypt

    text = requests.get(url).text
    codes = re.findall(
        r"DeObfuscate_String_and_Create_Form_With_Mhoa_URL\(\s*'(.*)'\s*,\s*'(.*)'\s*,\s*'(.*)'\s*,\s*'(.*)'\s*\)",
        text
    )
    assert len(codes) == 1 and len(codes[0]) == 4, "codes not found"
    d1, d2, name, size = codes[0]
    url = "https://download.megaup.net/?idurl={}&idfilename={}&idfilesize={}".format(encode(d1, d2), name, size)
    return url.replace(" ", "+")

def pack_megaup_url(url):
    text = requests.get(url).text
    url = re.findall(
        r'<a class=\"btn btn-default\" href=\"(.*)\">Create Download Link</a>',
        text
    )[0]
    return url.replace(" ", "+")