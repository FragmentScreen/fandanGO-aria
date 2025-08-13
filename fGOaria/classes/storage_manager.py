from fGOaria.classes.client_storage import StorageClient
from fGOaria.classes.client_provider import *
from fGOaria.classes import client_provider
from fGOaria.classes.storage_provider import StorageProvider

class StorageManager:
    """
    Manages available storage options for a given ARIA Entity ID
    """

    def __init__(self, aria_token: None, entity_id: str, entity_type: str):
        self._storage_client = StorageClient(aria_token, entity_id, entity_type)

    @property
    def providers(self) -> dict[str, StorageProvider]:
        """Get the available storage providers"""
        return self._storage_client.get_provider_options()

    @property
    def selected(self) -> StorageProvider:
        return self._selected

    @selected.setter
    def selected(self, provider: StorageProvider):
        self._selected = provider

    def select(self, client_option: str) -> ProviderClient:
        """Select a provider"""

        if (self.providers.get(client_option) is None):
            Exception(f"No provider option with id {client_option}")

        self._selected = self.providers.get(client_option)

        client = getattr(client_provider, client_option)
        self._client = client(self._selected)

        return self._client