from abc import ABC, abstractmethod
from ..utils.imports_config import *


class APIClient(ABC):
    """
    Generic API client class
    """

    def __init__(self, token):
        self.token = token

    @property
    @abstractmethod
    def base_url(self) -> str:
        pass

    @property
    @abstractmethod
    def headers(self) -> dict:
        pass

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        if params:
            query_string = self._construct_query_string(params)
            url += f"?{query_string}"
        resp = requests.get(url, headers=self.headers)
        resp.raise_for_status()
        return resp.json()

    def post(self, endpoint: str, data: dict = None):
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