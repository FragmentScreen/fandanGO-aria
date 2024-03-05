from .utils import get_formatted_datetime, print_with_spaces, check_headers, space
from .config import *
import yaml

load_dotenv('.env')
root_project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
config_path = os.path.join(root_project_dir, "config.yml")
with open(config_path, "r") as f:
    config = yaml.safe_load(f)

class OAuth :
    def __init__(self) -> None:
        self.grant_type = config["login"]["GRANT_TYPE"]
        self.scope = config["login"]["SCOPE"]
        self.client_id = config["login"]["CLIENT_ID"]
        self.url = config["login"]["LOGIN_URL"]
        self.client_secret = config["login"]["CLIENT_SECRET"]
        self.token_str_key = config["login"]["SESSION_KEY"]
        self.refresh_grant = config["login"]["REFRESH_GRANT"]


    def login(self, username, password) -> None:
        '''username and password passed from the commands 'login'. Gets login_data from pre-set env vars.'''
        login_data = self.get_login_data(username, password)
        try : 
            response = self.send_login_request(login_data)
            if response:
                self.handle_login_response(response)
        except Exception as e : 
            space()
            logging.error(f' Login to ARIA failed')
            print_with_spaces('Please check your credentials and try again.')
        

    def send_login_request(self, login_data) -> dict or None :
        try:
            response = requests.post(self.url, login_data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            raise

    
    def handle_login_response(self, response_data) -> None:
        '''
        Timestamps token data before storing on keychain for expiry comparison upon reuse
        '''
        response_data['TIMESTAMP'] = get_formatted_datetime()
        response_str = json.dumps(response_data)
        if response_str:
            click.echo('Successfully logged into ARIA.')
            self.set_token_data(response_str)
        else:
            logging.error('Error: Access token not found in the server response.')

    def set_token_data(self, token_data) -> bool or None :
        try :
            retrieval_password = click.prompt('Set token retrieval password', default='optional')
            retrieval_password = '' if retrieval_password == 'optional' else retrieval_password
            click.echo('Attempting to store Token...')
            keyring.set_password(self.token_str_key, retrieval_password, token_data)
            print_with_spaces('Token data successfully stored in keyring.')
        except key_err.PasswordSetError as e :
            logging.error(f"Error setting keyring: {e}")
        
        
    def get_access_token(self) -> dict or False :
        token_data = self.get_keyring_token_data()
        if token_data == False or not check_headers(token_data) :
            return False
        if self.check_token_valid(token_data['TIMESTAMP'], token_data['expires_in']) :
            return token_data
        elif self.check_token_valid(token_data['TIMESTAMP'], token_data['refresh_expires_in']) :
            print_with_spaces('Refreshing token..')
            token = self.refresh_token(token_data)
            if token :
                return token
        else : 
            print_with_spaces('Token expired. Please log back into ARIA')

    def get_keyring_token_data(self) -> dict or False :
        retrieval_pass = click.prompt('Enter your token password', default='optional')
        retrieval_pass = '' if retrieval_pass == 'optional' else retrieval_pass
        token_data_str = keyring.get_password(self.token_str_key, retrieval_pass)
        print('password worked')
        if not token_data_str :
            space()
            logging.error(' Either the password entered is incorrect, or no access token is stored.')
            print_with_spaces('Please login to ARIA to retrieve another token if the problem persists or type aria-help for more options.')
            return False
        return json.loads(token_data_str)
    
    def check_token_valid (self, token_timestamp_str, expiry) -> bool :
        current_time = datetime.now()
        token_timestamp = datetime.strptime(token_timestamp_str, '%Y-%m-%d %H:%M:%S')
        token_expiry_time = token_timestamp + timedelta(seconds=expiry)

        if current_time < token_expiry_time :
            return True
        
        return False
    
    def refresh_token(self, token_data) -> dict or False : 
        '''Posts refresh_token to retrieve new access_token. Some conversion between json string/object for storage and manipulation respectively '''
        refresh_token = token_data['refresh_token']
        refresh_data = self.get_refresh_data(refresh_token)
        try :
            response = requests.post(self.url, refresh_data)
            response.raise_for_status()
            response_data = response.json()
            response_data['TIMESTAMP'] = get_formatted_datetime()
            response_str = json.dumps(response_data)
            if response_str:
                # sort this out lu, the if block is a falsy even if true
                print_with_spaces('Successfully refreshed token')  
                if self.set_token_data(response_str) :
                    return json.loads(response_str)
                return json.loads(response_str)
            else :
                logging.error('Error: No token found in server response. If the problem persists, log back into ARIA.')
        except requests.exceptions.RequestException as e:
            click.echo('Login failed. Please check your credentials and try again.')
            logging.error(f'Error refreshing token: {e}')

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
