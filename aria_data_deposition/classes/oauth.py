import requests
import datetime
import keyring
import keyring.errors as key_err
import click
from dotenv import load_dotenv
import os
import json
from aria_data_deposition.utils import get_formatted_datetime, print_with_spaces

load_dotenv('.env.dev')

class OAuth :
    def __init__(self):
        self.grant_type = os.getenv("GRANT_TYPE")
        self.scope = os.getenv("SCOPE")
        self.client_id = os.getenv("CLIENT_ID")
        self.url = os.getenv("LOGIN_URL")
        self.client_secret = os.getenv("CLIENT_SECRET")
        self.token_str_key = os.getenv("SESSION_KEY")


    def get_login_data(self, username, password) :
        return {
            'grant_type': self.grant_type,
            'scope': self.scope,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'username': username,
            'password': password
        }

    def login(self, username, password) -> None :
        login_data = self.get_login_data(username, password)

        try:
            response = requests.post(self.url, login_data)
            response.raise_for_status()
            response_data = response.json()
            response_data['TIMESTAMP'] = get_formatted_datetime()
            response_str = json.dumps(response_data)
            if response_str:
                print_with_spaces('Successfully logged into ARIA. Set a password to retrieve your access token when performing commands that interact with ARIA.')    
                self.set_token_data(response_str)
            else:
                click.echo('Error: Access token not found in the server response.')
        except requests.exceptions.RequestException as e:
            click.echo(f'Error: {e}')
            click.echo('Login failed. Please check your credentials and try again.')


    def set_token_data(self, token_data) -> None :
        try :
            retrieval_password = click.prompt('Set token retrieval password', default='optional')
            retrieval_password = '' if retrieval_password == 'optional' else retrieval_password
            click.echo('Attempting to store Token...')
            keyring.set_password(self.token_str_key, retrieval_password, token_data)
            print_with_spaces('Token data successfully stored in keyring.')
        except key_err.PasswordSetError as e :
            click.echo(f"Error setting keyring: {e}")
        
        
    def get_access_token(self) -> object or False :
        token_data = self.get_keyring_token_data()

        # if not self.token_keys_exist(token_data) :
        #     click.echo('Keyring Error: Please log back into ARIA.')
        #     return False

        if not token_data['TIMESTAMP'] or not token_data['expires_in'] :
            click.echo('Keyring Error: Please log back into ARIA.')
            return False
        
        if self.check_token_valid(token_data['TIMESTAMP'], token_data['expires_in']) :
            click.echo('Token valid')
            return token_data['access_token']
        else:
            click.echo('Token Expired')
    
    def get_keyring_token_data(self) -> object or False :
        retrieval_pass = click.prompt('Enter your token password', default='optional')
        retrieval_pass = '' if retrieval_pass == 'optional' else retrieval_pass
        token_data_str = keyring.get_password(self.token_str_key, retrieval_pass)
        if not token_data_str :
            click.echo('Error: Either the password entered is incorrect, or no access token is stored.')
            print_with_spaces('Please login to ARIA to retrieve another token if the problem persists or type aria-help for more options.')
            return False
        token_data_obj = json.loads(token_data_str)
        return token_data_obj
    
    # enter pass
    # get it 
    # check timestamp
    # if no, refresh token_str_key
    # if stamp gone - error
    
    def check_token_valid (self, token_timestamp_str, expiry) -> bool :

        current_time = datetime.datetime.now()
        token_timestamp = datetime.datetime.strptime(token_timestamp_str, '%Y-%m-%d %H:%M:%S')
        token_expiry_time = token_timestamp + datetime.timedelta(seconds=expiry)

        if current_time < token_expiry_time :
            return True
        
        return False