class Client:
    def __init__(self, oauth):
        self.oauth = oauth

    def authenticate(self, username, password):
        self.oauth.login(username, password)

    def get_access_token(self):
        return self.oauth.get_access_token()

    # TODO: 
    # - Add more methods for interacting with the API using the access token
