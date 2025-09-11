import requests

BASE_URL = "https://api.example.com/data"

def fetch_data(endpoint):
    response = requests.get(f"{BASE_URL}/{endpoint}")
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def post_data(endpoint, data):
    response = requests.post(f"{BASE_URL}/{endpoint}", json=data)
    if response.status_code == 201:
        return response.json()
    else:
        response.raise_for_status()

def delete_data(endpoint):
    response = requests.delete(f"{BASE_URL}/{endpoint}")
    if response.status_code == 204:
        return True
    else:
        response.raise_for_status()