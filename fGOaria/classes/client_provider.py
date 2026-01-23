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
        self._file_id = None
        super().__init__(self._token.access_token)

    @property
    def _token(self) -> Token:
        return self._provider.credentials.token

    @property
    def host_endpoint(self) -> str:
        return self._provider.credentials.host_endpoint

    @property
    def file_id(self) -> str or None:
        return self._file_id if self._file_id else None

    def _set_file_id(self, file_id: str):
        self._file_id = file_id

    @abstractmethod
    def file_locate(self, file_id: str) -> object:
        """Get the location details of a file"""
        pass

    @abstractmethod
    def file_upload(self, file_location: str) -> object:
        """Push file to external storage provider"""
        pass

    @abstractmethod
    def get_file_id(self, filename: str) -> str:
        """Get the ID of a file from its filename"""
        pass

    @abstractmethod
    def file_download(self, file_id: str or None, dest_path) -> object:
        """Download file from external storage provider"""
        pass

    @abstractmethod
    def file_delete(self, file_id: str):
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
    def base_data_endpoint(self) -> str:
        return "oneprovider/data"

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
        """Get the details of the current OneData data space"""
        return self.get(self.space_endpoint)

    def file_locate(self, file_id: str) -> object:
        """@todo find the location of the file on OneData"""
        pass

    def file_upload(self, filename: str) -> object:
        """Upload a file to OneData"""

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

    def get_file_id(self, filename: str) -> str:
        """Find the OneData file ID by filename."""
        endpoint = f"{self.data_endpoint}/children?"
        try:
            response = self.get(endpoint)
        except Exception as e:
            raise ConnectionError(f"Error fetching children: {e}")

        files = response.get("children", []) or response.get("entries", [])
        for f in files:
            if f.get("name") == filename:
                self._set_file_id(f.get("file_id"))
                return f.get("file_id")

        raise FileNotFoundError(f"File '{filename}' not found in OneData.")

    def file_download(self, file_id: str or None = None, dest_path) -> object:

        if file_id is None and self.file_id is not None:
            file_id = self.file_id

        if file_id is None:
            raise Exception("No file id provided.")

        endpoint = f"{self.base_url}/{self.base_data_endpoint}/{file_id}/content"
        result = super().download(self, endpoint, dest_path)

        return result

    def file_delete(self, file_id: str or None = None) -> int:
        """Delete a file from the OneData data space"""

        if file_id is None and self.file_id is not None:
            file_id = self.file_id

        if file_id is None:
            raise Exception("No file id provided.")

        endpoint = f"{self.base_data_endpoint}/{file_id}"

        try:
            resp = super().delete(endpoint)
        except Exception as e:
            raise ConnectionError(f"Error deleting file '{file_id}' (Likely file not found): {e}")

        return resp.status_code

    def _handle_http_errors(self, error: HTTPError, context: str):
        response = error.response.content
        if isinstance(response, str) and json.loads(response) is not None:
            details = json.loads(response).get('error')
            if details is not None:
                error.response.message = details
                raise HTTPError(f"Error {context} \"{details.id}\": {details.description}.")
        raise error
