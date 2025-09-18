from types import MappingProxyType
from fGOaria.classes import client_provider
from fGOaria.classes.client_storage import StorageClient
from fGOaria.classes.storage_provider import StorageProvider

PROVIDER_CLIENT_MAP = MappingProxyType({
    'ARIA\\Storage\\StorageEngines\\OneDataStorageEngine': client_provider.OneDataClient
})

class StorageManager:
    """
    Manages available storage options for a given ARIA Entity ID
    """

    def __init__(self, aria_token: str, entity_id: str, entity_type: str = 'visit'):
        self._storage_client = StorageClient(aria_token, entity_id, entity_type)
        self._provider_client = None

    @property
    def providers(self) -> dict[str, StorageProvider]:
        """Get the available storage providers"""
        return self._storage_client.options

    @property
    def selected(self) -> StorageProvider:
        """The currently selected storage provider"""
        return self._selected

    @property
    def client(self) -> client_provider.ProviderClient or None:
        """The client for the currently selected storage provider"""
        return self._provider_client

    def select(self, provider_id: str):
        """Select a provider"""
        if self.providers.get(provider_id) is None:
            raise Exception(f"No provider option with id {provider_id}")
        self._selected = self.providers.get(provider_id)

    def provision(self):
        """Provision storage on the currently selected storage provider"""
        self._selected.credentials = self._storage_client.get_provider_credentials(self._selected.id)

        client = PROVIDER_CLIENT_MAP[self._selected.type]
        self._provider_client = client(self._selected)
