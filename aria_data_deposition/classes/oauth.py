import requests
import keyring
import click
from dotenv import load_dotenv
import os

load_dotenv('.env.production')

class OAuth:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        url = os.getenv("LOGIN_URL")
        login_data = {
            'grant_type': os.getenv("GRANT_TYPE"),
            'scope': os.getenv("SCOPE"),
            'client_id': os.getenv("CLIENT_ID"),
            'client_secret': os.getenv("CLIENT_SECRET"),
            'username': self.username,
            'password': self.password
        }

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
