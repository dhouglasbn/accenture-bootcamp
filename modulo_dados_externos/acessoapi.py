import requests
import json

response = requests.get("https://swapi.info/api/films")
content = response.text

with open('swapi.json', 'w') as file:
  json.dump(content, file)

with open('swapi.json', 'r') as file:
  result = json.load(file)

print(result)