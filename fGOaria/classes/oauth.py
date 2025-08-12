from ..utils.utility_functions import get_formatted_datetime, print_with_spaces, check_headers, space
from .client_oauth import AriaOauthClient
from ..utils.imports_config import *
from .token import Token
from ..utils.encryption import TokenEncryption
from pathlib import Path


class OAuth :
    def __init__(self) -> None:
        self.client = AriaOauthClient()
        self.username = os.getenv('ARIA_CONNECTION_USERNAME')
        self.password = os.getenv('ARIA_CONNECTION_PASSWORD')
        self.grant_type = os.getenv('ARIA_CONNECTION_GRANT_TYPE')
        self.scope = os.getenv('ARIA_CONNECTION_SCOPE')
        self.client_id = os.getenv('ARIA_CLIENT_ID')
        self.url = os.getenv('ARIA_CONNECTION_LOGIN_URL')
        self.client_secret =  os.getenv('ARIA_CLIENT_SECRET')
        self.token_str_key = os.getenv('ARIA_KEYRING')
        self.refresh_grant = os.getenv('ARIA_CONNECTION_REFRESH_GRANT')
        self.token_encryption = TokenEncryption()
        self.token_file = Path.home() / '.aria_token.json'


    # LOGIN

    def login(self, username, password) -> None:
        '''username and password passed from the commands 'login'. Gets login_data from pre-set config vars.'''
        self.username = username if username is not None else self.username
        self.password = password if password is not None else self.password
        login_data = self.get_login_data(self.username, self.password)
        try : 
            response = self.client.login(login_data)
            self.handle_auth_response(response)
            click.echo('Successfully logged into ARIA.')
        except Exception as e : 
            logging.error(f' Login to ARIA failed : {e.args}')
            print_with_spaces('Please check your credentials and try again.')


    # AUTH HANDLING
    
    def handle_auth_response(self, response_data) -> Token:
        '''
        Timestamps token data before storing on keychain for expiry comparison upon reuse
        '''
        token = Token(response_data)
        token.timestamp = get_formatted_datetime()
        self.set_token_keyring_data(token)
        return token


    # TOKEN 
        
    def get_access_token(self) -> Union[dict, None]:
        token_data = self.get_keyring_token_data()
        
        if token_data is None or not check_headers(token_data):
            raise Exception("Failed to fetch token.")

        token = Token(token_data)
        if token.is_valid():
            return token
        elif token.is_valid(True) :
            print_with_spaces('Refreshing token..')
            return self.refresh_token(token)
        else:
            raise Exception("Token expired. Please log back into ARIA")
    
    def refresh_token(self, token : Token) -> Union[Token, None] : 
        '''Posts refresh_token to retrieve new access_token. Some conversion between json string/object for storage and manipulation respectively '''
        refresh_token = token.refresh_token
        refresh_data = self.get_refresh_data(refresh_token)
        try :
            token_data = self.client.login(refresh_data)
            token = self.handle_auth_response(token_data)
            return token
        except requests.exceptions.RequestException as e:
            click.echo('Login failed. Please check your credentials and try again.')
            logging.error(f'Error refreshing token: {e}')


    #  KEYRING STORAGE
            
    def get_keyring_token_data(self) -> Union[dict, None] :
        try:
            token_data_str = keyring.get_password(self.token_str_key, '')
            if token_data_str:
                print_with_spaces('Token data successfully retrieved from keyring.')
                return json.loads(token_data_str)
        except Exception as e:
            logging.warning(f"Keyring storage failed: {e}")

        try:
            token_data = self.token_encryption.decrypt_token(self.password)
            print_with_spaces('Token data successfully retrieved from encrypted storage.')
            if token_data:
                return token_data
        except Exception as e:
            logging.warning(f"Encrypted storage failed: {e}")

        try:
            token_data = self.get_json_token_data()
            print_with_spaces('Token data successfully retrieved from JSON file.')
            if token_data:
                return token_data
        except Exception as e:
            logging.warning(f"JSON file storage failed: {e}")

        raise Exception('No access token found in any storage method.')
    
    def set_token_keyring_data(self, token : Token) -> None :
        click.echo('Attempting to store Token...')
        token_json = json.dumps(token.to_dict())
        
        try:
            keyring.set_password(self.token_str_key, '', token_json)
            print_with_spaces('Token data successfully stored in keyring.')
            return
        except Exception as e:
            logging.warning(f"Keyring storage failed: {e}")

        try:
            self.token_encryption.encrypt_token(token.to_dict(), self.password)
            print_with_spaces('Token data successfully stored using encryption.')
            return
        except Exception as e:
            logging.warning(f"Encrypted storage failed: {e}")

        try:
            self.set_json_token_data(token.to_dict())
            print_with_spaces('Token data successfully stored in JSON file.')
            return
        except Exception as e:
            logging.warning(f"JSON file storage failed: {e}")

        raise Exception("Failed to store token in any available storage method.")

    def get_json_token_data(self) -> Union[dict, None]:
        """Retrieve token data from JSON file storage."""
        try:
            if self.token_file.exists():
                with open(self.token_file, 'r') as f:
                    return json.load(f)
            return None
        except Exception as e:
            logging.error(f"Error reading JSON token file: {e}")
            return None

    def set_json_token_data(self, token_data: dict) -> None:
        """Store token data in JSON file storage."""
        try:
            with open(self.token_file, 'w') as f:
                json.dump(token_data, f)
        except Exception as e:
            logging.error(f"Error writing JSON token file: {e}")
            raise Exception("Failed to write token to JSON file storage.")


    # GET DATA OBJECTS
            
    def get_login_data(self, username, password) -> dict :
        return {
            'grant_type': self.grant_type,
            'scope': self.scope,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'username': username,
            'password': password
        }
    
    def get_refresh_data(self, refresh_token) -> dict :
        return {
                'grant_type': self.refresh_grant,
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'refresh_token': refresh_token
        }
