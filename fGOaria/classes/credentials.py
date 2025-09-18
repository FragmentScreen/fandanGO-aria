from fGOaria.classes.token import Token

class Credentials:
    """
    Represents the credentials required to connect to a client
    """

    def __init__(self, host_endpoint: str, token: Token, options: dict or None = None):
        self._host_endpoint = host_endpoint
        self._token = token
        self._options = options

    @property
    def host_endpoint(self) -> str:
        return self._host_endpoint

    @property
    def token(self) -> Token:
        return self._token

    @property
    def options(self) -> dict:
        return self._options

    @options.setter
    def options(self, options: dict):
        self._options = options
