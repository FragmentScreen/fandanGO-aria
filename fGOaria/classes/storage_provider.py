from fGOaria.classes.credentials import Credentials

class StorageProvider():
    """
    Represents a storage provider option
    """

    def __init__(self, provider_id: str, name: str, description: str, provider_type: str, credentials: Credentials = None):
        self._id = provider_id
        self._name = name
        self._description = description
        self._type = provider_type
        self._credentials = credentials

    def __dict__(self) -> dict[str, str]:
        return {
            'name': self._name,
            'description': self._description,
            'type': self._type
        }

    def __repr__(self) -> str:
        return str(self.__dict__())

    @property
    def id(self) -> str:
        """Getter for the Provider ID."""
        return self._id

    @property
    def name(self) -> str:
        """Getter for the name of the provider."""
        return self._name

    @property
    def description(self) -> str:
        """Getter for the description of the provider."""
        return self._description

    @property
    def type(self) -> str:
        """Getter for the description of the provider."""
        return self._type

    @property
    def credentials(self) -> Credentials:
        """Get credentials from my provider."""
        return self._credentials

    @credentials.setter
    def credentials(self, credentials: Credentials):
        """Setter for the description of the provider."""
        self._credentials = credentials