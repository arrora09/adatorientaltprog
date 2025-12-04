import requests

url = "http://python.org"

r = requests.get(url)

print(r)

html = r.text

print(html)
