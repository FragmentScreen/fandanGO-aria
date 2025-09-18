from abc import ABC
from fGOaria.classes.api_client import APIClient
from fGOaria.utils.imports_config import *
from dotenv import load_dotenv

load_dotenv()

class AriaClient(APIClient, ABC):
    """
    Abstract client to interface with ARIA's APIs, extend for specific APIs such as access/data mgmt, etc
    """

    def __init__(self, token: str):
        super().__init__(token)
        self.dev = os.getenv('DEV', 'LOCAL')
        if self.dev == 'LOCAL':
            self.aria_login_url = os.getenv('ARIA_CONNECTION_LOGIN_URL_LOCAL')
        else:
            self.aria_login_url = os.getenv('ARIA_CONNECTION_LOGIN_URL')

    @property
    def base_url(self) -> str:
        return os.getenv(f'ARIA_GQL_{self.dev}')

    @property
    def headers(self) -> dict:
        return {'Authorization': f'Bearer {self.token}'} if self.token else None
