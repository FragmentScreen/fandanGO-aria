import requests
from .config import API_URLS
from .utils import set_headers, pretty_print

class APIClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        headers = set_headers(self.token)
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        return resp.json()

    def post(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        headers = set_headers(self.token)
        resp = requests.post(url, json=data, headers=headers)
        resp.raise_for_status()
        return resp.json()

    # Add other HTTP methods as needed (e.g., PUT, DELETE)