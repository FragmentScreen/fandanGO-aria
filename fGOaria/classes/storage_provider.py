class StorageProvider():
    def __init__(self, provider_id: str, name: str, description: str, credentials: dict):
        self._id = provider_id
        self._name = name
        self._description = description
        self._credentials = credentials

    @property
    def provider_id(self) -> str:
        """Getter for the Provider ID."""
        return self._provider_id

    @provider_id.setter
    def provider_id(self, value):
        """Setter for the Provider ID."""
        self._provider_id = value

    @property
    def name(self) -> str:
        """Getter for the name of the provider."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for the name of the provider."""
        self._name = value

    @property
    def description(self) -> str:
        """Getter for the description of the provider."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for the description of the provider."""
        self._description = value

    @property
    def credentials(self) -> dict:
        """Get credentials from my provider."""
        return self._credentials

    @credentials.setter
    def credentials(self, value):
        """Setter for the description of the provider."""
        self._credentials = value