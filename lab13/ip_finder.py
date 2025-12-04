import requests
import json

response = requests.get("https://jsonip.com/")

d = json.loads(response.text)
print(f"Az Ön IP címe: {d["ip"]}")
