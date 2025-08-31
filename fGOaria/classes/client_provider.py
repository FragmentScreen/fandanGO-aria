from .api_client import APIClient
from .token import Token
from .storage_provider import StorageProvider
from abc import ABC, abstractmethod

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
    def provider_host(self) -> str:
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
    def data_space(self) -> dict:
        """Get the details of the provider's available data space"""
        pass

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
        self.space_id = provider.credentials.options.get('space_id')

    @property
    def base_url(self) -> str:
        return f"{self.provider_host}/api/v3"

    @property
    def space_endpoint(self) -> str:
        return f"onezone/spaces/{self.space_id}"

    @property
    def data_endpoint(self) -> str:
        return f"oneprovider/data/{self.space_id}"

    @property
    def headers(self):
        return {'x-auth-token': self.token} if self.token else None

    def data_space(self) -> dict:
        """
        Get the details of the current OneData data space
        """
        return self.get(self.space_endpoint)

    def locate(self, file_id) -> object:
        """@todo find the location of the file on OneData"""
        pass

    def upload(self, filename) -> object:
        """@todo get this working"""
        self.headers['Content-Type'] = 'application/octet-stream'
        endpoint = f"{self.data_endpoint}/children?name={filename}&override=true"
        with open(filename, 'rb') as file:
            response = self.post(endpoint, {'file': file})
        print(f"Push: {response.status_code} - {response.text}")
        # TODO: handle bad status codes
        if response.status_code in range(200, 300):
            self._file_id = response.file_id
        return response

    def download(self, file_id) -> object:
        """@todo """
        pass

    def delete(self, file_id) -> object:
        """@todo"""
        pass
