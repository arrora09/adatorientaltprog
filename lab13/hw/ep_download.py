import json
from PIL import Image
import requests
from io import BytesIO

data = requests.get("http://www.reddit.com/r/earthporn/.json")

d = json.loads(data.text)


for obj in d["data"]["children"]:
    url = obj["data"]["url"]

    response = requests.get(url)

    img = Image.open(BytesIO(response.content))

    print(url, img.size)
