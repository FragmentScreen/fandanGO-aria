from abc import ABC, abstractmethod
from requests import Response
from ..utils.imports_config import *


class APIClient(ABC):
    """
    Generic API client class
    """

    def __init__(self, token: str):
        self.token = token

    @property
    @abstractmethod
    def base_url(self) -> str:
        pass

    @property
    def headers(self) -> dict:
        return self.headers

    @headers.setter
    def headers(self, value):
        self.headers = {'Authorization': f'Bearer {self.token}'} if self.token else None

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        if params:
            query_string = self._construct_query_string(params)
            url += f"?{query_string}"
        resp = requests.get(url, headers=self.headers)
        resp.raise_for_status()
        return resp.json()

    def post(self, endpoint: str, data: any = None, json: bool = True):
        url = f"{self.base_url}/{endpoint}"
        if (json is True and not isinstance(data, dict)):
            raise Exception("To post non-JSON data, set `json=False`")
        resp = requests.post(url=url,
                             data=data if json is False else None,
                             json=data if json is True else None,
                             headers=self.headers)
        resp.raise_for_status()
        return resp.json()

    def delete(self, endpoint) -> Response:
        url = f"{self.base_url}/{endpoint}"
       
        # Copy and prepare headers
        headers = getattr(self, "headers", {}).copy()
 
        resp = requests.delete(url, headers=headers, timeout=10)
        resp.raise_for_status()
        return resp

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