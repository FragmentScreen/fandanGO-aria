import json
from urllib import parse
from abc import ABC, abstractmethod
from requests.exceptions import HTTPError
from fGOaria.classes.api_client import APIClient
from fGOaria.classes.token import Token
from fGOaria.classes.storage_provider import StorageProvider


class ProviderClient(APIClient, ABC):
    """
    Abstract storage provider client class. Clients for external storage providers should inherit from this class.
    """

    def __init__(self, provider: StorageProvider):
        self._provider = provider
        super().__init__(self._token.access_token)

    @property
    def _token(self) -> Token:
        return self._provider.credentials.token

    @property
    def host_endpoint(self) -> str:
        return self._provider.credentials.host_endpoint

    @property
    def file_id(self) -> str:
        return self._file_id

    @property
    def _file_id(self) -> str: # this may seem redundant, but is required for a protected setter
        return self._file_id

    @_file_id.setter
    def _file_id(self, file_id: str):
        self._file_id = file_id

    @abstractmethod
    def locate(self, file_id) -> object:
        """Get the location details of the file"""
        pass

    @abstractmethod
    def upload(self, file_location) -> object:
        """Push file to external storage provider"""
        pass

    @abstractmethod
    def download(self, file_id) -> object:
        """Download file from external storage provider"""
        pass

    @abstractmethod
    def delete(self, file_id) -> object:
        """Delete file from external storage provider"""
        pass


class OneDataClient(ProviderClient):
    """
    Provider client for OneData
    """

    def __init__(self, provider: StorageProvider):
        super().__init__(provider)
        self.token_type = provider.credentials.token.token_type
        self.space_id = provider.credentials.options.get('space_id')

    @property
    def base_url(self) -> str:
        return f"{self.host_endpoint}"

    @property
    def space_endpoint(self) -> str:
        return f"onezone/spaces/{self.space_id}"

    @property
    def data_endpoint(self) -> str:
        return f"oneprovider/data/{self.space_id}"

    @property
    def headers(self):
        return {
            self.token_type: self.token,
            'content-type': 'application/octet-stream',
        } if self.token else None

    def data_space(self) -> dict:
        """
        Get the details of the current OneData data space
        """
        return self.get(self.space_endpoint)

    def locate(self, file_id) -> object:
        """@todo find the location of the file on OneData"""
        pass

    def upload(self, filename) -> str:
        """
        Upload a file to OneData
        :param filename: filename to upload
        :return: OneData file_id
        """

        endpoint = f"{self.data_endpoint}/children?"
        options = parse.urlencode({
            # 'spaceId': self.space_id,
            'name': filename,
            'override': 'true'
        })

        with open(filename, 'rb') as file:
            if file is None:
                raise FileNotFoundError("File not found.")
            try:
                response = self.post(f"{endpoint}{options}", data=file, json=False)
            except HTTPError as e:
                self._handle_http_errors(e, "uploading file")

        return response

    def download(self, file_id) -> object:
        """@todo """
        pass

    def delete(self, file_id) -> object:
        """@todo"""
        pass

    def _handle_http_errors(self, error: HTTPError, context: str):
        response = error.response.content
        if isinstance(response, str) and json.loads(response) is not None:
            details = json.loads(response).get('error')
            if details is not None:
                error.response.message = details
                raise HTTPError(f"Error {context} \"{details.id}\": {details.description}.")
        raise error
