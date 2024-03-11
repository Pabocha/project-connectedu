import requests

endpoint = "http://localhost:8000/salle/"
headers = {
    'Host': 'belle-rose.localhost'
}
response = requests.get(endpoint, headers=headers)

print(response.json())