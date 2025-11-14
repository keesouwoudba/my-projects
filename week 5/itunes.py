import json
import requests


name = input("name: ")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=2&term=" + name)

o = response.json()
for result in o["results"]:
    print(result["trackName"])

o = json.dumps(o, indent=2)
print(o)