from dotenv import load_dotenv
from fGOaria.classes.api_client import APIClient
from fGOaria.utils.imports_config import *
from fGOaria.utils.utility_functions import set_headers

load_dotenv()

class AriaRest(APIClient):
    """
    Abstract client to interface with ARIA's REST APIs
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
        return os.getenv(f'ARIA_REST_{self.dev}')

    @property
    def headers(self) -> dict:
        headers = set_headers(self.token) if self.token else {}
        headers['Accept'] = 'application/json'
        return headers

    def upload(self, file_name: str, file_type: str = None) -> object:
        """Upload a file to ARIA"""
        if not os.path.exists(file_name):
            raise FileNotFoundError(f"File \"{file_name}\" not found.")

        if os.path.getsize(file_name) > 104857600:
            raise Exception(f"File \"{file_name}\" is too large. The maximum file size is 100MB.")

        with open(file_name, 'rb') as file:
            data = {
                'random': 'true',
                'randomlength': '32',
                'filetype': file_type or ''
            }
            files = {
                'files[]': (os.path.basename(file_name), file, file_type or 'application/octet-stream')
            }
            resp = requests.post(f"{self.base_url}/files/file", data=data, files=files, headers=self.headers)
            resp.raise_for_status()
            return resp.json()
