import os
from dotenv import load_dotenv
from typing import Dict
from fGOaria.classes.aria_client import AriaClient
from fGOaria.classes.credentials import Credentials
from fGOaria.classes.storage_provider import StorageProvider
from fGOaria.classes.token import Token
# from fGOaria.utils.queries import GET_STORAGE_PROVIDERS, FETCH_STORAGE_TOKENS, CHECK_STORAGE_VALIDITY


load_dotenv()

class StorageClient(AriaClient):
    """
    APIClient for ARIA's storage manager API
    @todo currently a stub, still to be hooked up to actual API
    """

    def __init__(self, token, entity_id: str, entity_type: str):
        super().__init__(token)
        self.id = entity_id
        self.type = entity_type

    def get_provider_options(self) -> Dict[str, StorageProvider]:
        """
        Retrieve all available storage provider options
        @todo use ARIA storageProviders query
        """
        print(f'Getting provider options for {self.type} ID {self.id}')
        return {'OneDataClient': StorageProvider(
            provider_id='1',
            name="OneData",
            description="High-performance data management solution",
            credentials=Credentials(
                host_endpoint=os.getenv("ONEDATA_HOST_ENDPOINT"),
                token=self.get_provider_token('1'),
                options={'space_id': os.getenv("ONEDATA_SPACE_ID")}
            )
        )}

    def get_provider_token(self, provider_id: str) -> Token or None:
        """
        Retrieve the token for a specific provider
        @todo use ARIA getStorageTokens mutation
        """
        print(f'Pulling token')
        return Token({
            'access_token': os.getenv("ONEDATA_ACCESS_TOKEN"),
            'expires_in': None,
            'refresh_expires_in': None,
            'refresh_token': None,
            'token_type': None,
            'not-before-policy': None,
            'session_state': None,
            'scope': None,
            'timestamp': None,
        }) if provider_id == '1' else None
