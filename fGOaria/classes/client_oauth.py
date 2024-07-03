from .api_client import APIClient
from ..utils.imports_config import *

class ClientOauth(APIClient) :

    def __init__(self, token=None):
        super().__init__(token)

    def login(self, login_data) :
        response = requests.post(self.aria_login_url, login_data)
        response.raise_for_status()
        response = response.json()
        return response

