import requests
import keyring
import click
from dotenv import load_dotenv
import os

load_dotenv('.env.dev')

class OAuth :
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.grant_type = os.getenv("GRANT_TYPE")
        self.scope = os.getenv("SCOPE")
        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")

    def get_login_data(self) :
        return {
            'grant_type': self.grant_type,
            'scope': self.scope,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'username': self.username,
            'password': self.password
        }

    def login(self):
        url = os.getenv("LOGIN_URL")
        login_data = self.get_login_data()

        try:
            response = requests.post(url, login_data)
            response.raise_for_status()
            response_data = response.json()
            token = response_data.get('access_token')
            if token:
                keyring.set_password('aria_oauth', self.username, token)
                click.echo(f'Successfully logged into ARIA. Access Token: {token}')
            else:
                click.echo('Error: Access token not found in the server response.')
        except requests.exceptions.RequestException as e:
            click.echo(f'Error: {e}')
            click.echo('Login failed. Please check your credentials and try again.')
