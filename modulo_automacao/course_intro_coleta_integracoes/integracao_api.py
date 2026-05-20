import requests

url = "https://api.agify.io/?name=ana"

response = requests.get(url)

data = response.json()

print(data)