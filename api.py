import requests

rispans = requests.get(url='http://api.open-notify.org/iss-now.json')
rispans.raise_for_status()

data = rispans.json()
print(data)
print(type(data))
print(data['timestamp'])
print(type(data['timestamp']))