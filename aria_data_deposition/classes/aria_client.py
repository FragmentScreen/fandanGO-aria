from .oauth import OAuth

class AriaClient:
    @staticmethod
    def login(username, password):
        oauth_instance = OAuth(username, password)
        oauth_instance.login()