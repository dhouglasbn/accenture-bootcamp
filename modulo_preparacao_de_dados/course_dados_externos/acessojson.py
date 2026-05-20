import json

data = {
  "colors": {
    "0": "red",
    "1": "orange",
    "2": "yellow",
    "3": "green",
    "4": "cyan",
    "5": "blue",
    "6": "purple"
  }
}

with open('data.json', 'w') as file:
  json.dump(data, file)

with open('data.json', 'r') as file:
  content = json.load(file)

print(content)