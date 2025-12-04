import urllib.request


def get_page(url: str) -> str:
    response = urllib.request.urlopen(url)

    raw = response.read()

    # print(type(raw))
    # print(raw)
    print(raw)
    html = raw.decode("utf-8")
    print(html)
    # print(html[:200])
    return html
