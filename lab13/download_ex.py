import urllib.request
import certifi
import ssl


def main():
    url = "https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php"
    # url = "http://python.org"
    context = ssl.create_default_context(cafile=certifi.where())
    response = urllib.request.urlopen(url, context=context)

    raw = response.read()

    print(type(raw))
    print(raw)
    html = raw.decode("utf-8")
    print(html[:200])


if __name__ == "__main__":
    main()
