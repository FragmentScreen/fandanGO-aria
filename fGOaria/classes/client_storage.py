import os
from dotenv import load_dotenv
from fGOaria.classes.aria_client import AriaClient
from fGOaria.classes.credentials import Credentials
from fGOaria.classes.storage_provider import StorageProvider
from fGOaria.classes.token import Token
from fGOaria.utils.queries import GET_STORAGE_PROVIDERS, FETCH_STORAGE_TOKENS, CHECK_STORAGE_VALIDITY

load_dotenv()

class StorageClient(AriaClient):
    """
    API client for ARIA's storage brokering API
    """

    def __init__(self, token: str, entity_id: str, entity_type: str = 'visit'):
        super().__init__(token)
        self.id = entity_id
        self.type = entity_type
        self._options = None

    @property
    def options(self) -> dict[str, StorageProvider]:
        """
        Retrieve all available storage provider options
        """
        if self._options is None:
            self._get_provider_options()
        return self._options

    def _get_provider_options(self):
        """
        Pull latest list of storage provider options from ARIA
        @todo Handle pagination (by default only gets 1st page / 10 max results)
        """
        results = self.gql_query(GET_STORAGE_PROVIDERS.query)

        if (results is None):
            raise Exception("Couldn't pull results ARIA's storage brokering API")

        options = results['data'][GET_STORAGE_PROVIDERS.return_key]['nodes']

        self._options = {}
        for option in options:
            self._options[option['id']] = StorageProvider(
                provider_id=option['id'],
                name=option['name'],
                description=option['description'],
                provider_type=option['engine']
            )

    def get_provider_credentials(self, provider_id: str) -> Credentials or None:
        """
        Retrieve the token for a specific provider
        """
        try:
            self.check_provider_validity(provider_id)
        except Exception as e:
            raise Exception(f"Cannot provision storage to this provider: {e}")

        results = self.gql_query(FETCH_STORAGE_TOKENS.mutation, {
            'input': {
                'storageProviderId': provider_id,
                'visit_id': self.id
            }
        })

        provider_token = results['data'][FETCH_STORAGE_TOKENS.return_key]
        token = Token(provider_token['token'])

        return Credentials(
            host_endpoint=provider_token['token']['host_endpoint'],
            token=token,
            options={
                key: val for key, val in provider_token['token'].items()
                if key not in ['host_endpoint', *(token.to_dict().keys())]
            }
        ) if provider_token['token'] else None

    def check_provider_validity(self, provider_id: str):
        """
        Check if storage can be provisioned by this provider for this visit
        @todo hook up to CHECK_STORAGE_VALIDITY mutation
        """
        if self.type != 'visit':
            raise Exception('The ARIA storage broker currently only accepts visit IDs')
