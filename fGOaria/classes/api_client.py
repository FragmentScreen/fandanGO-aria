from ..utils.imports_config import *
from ..utils.utility_functions import set_headers, get_config
from dotenv import load_dotenv

load_dotenv()
class APIClient:
    def __init__(self, token):
        self.token = token
        self.dev = os.getenv('DEV', 'LOCAL')
        if self.dev == 'LOCAL':
            self.aria_login_url = os.getenv('ARIA_CONNECTION_LOGIN_URL_LOCAL')
        else: 
            self.aria_login_url = os.getenv('ARIA_CONNECTION_LOGIN_URL')
        self.headers = set_headers(self.token) if self.token else None
        self.base_url = os.getenv(f'ARIA_GQL_{self.dev}')

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        if params:
            query_string = self._construct_query_string(params)
            url += f"?{query_string}"
        resp = requests.get(url, headers=self.headers)
        resp.raise_for_status()
        return resp.json()

    def post(self, endpoint : str, data : dict = None):
        resp = requests.post(endpoint, json=data, headers=self.headers)
        resp.raise_for_status()
        return resp.json()
    

    def gql_query(self, query: str, variables: dict = None):
        """GraphQL POST request."""
        payload = {"query": query}
        if variables:
            payload["variables"] = variables
        response = requests.post(self.base_url, json=payload, headers=self.headers)
        json_resp = response.json()
        if 'errors' in json_resp:
            error_message = f"GraphQL Errors: {json_resp['errors']}"
            raise Exception(error_message)
        return json_resp

    def _construct_query_string(self, params):
        query_string_parts = []
        for key, value in params.items():
            if value is None or (isinstance(value, list) and None in value):
                continue
            if isinstance(value, (list, tuple)):
                for item in value:
                    query_string_parts.append(f"filter[{key}][]={item}")
            else:
                query_string_parts.append(f"filter[{key}]={value}")
        query_string = "&".join(query_string_parts)
        return query_string