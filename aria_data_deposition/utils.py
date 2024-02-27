from .config import *

def get_formatted_datetime(input_datetime=None, format_str='%Y-%m-%d %H:%M:%S'):
    if input_datetime is None:
        input_datetime = datetime.now()

    formatted_datetime = input_datetime.strftime(format_str)
    return formatted_datetime

def print_with_spaces(str) :
    click.echo('')
    click.echo(str)
    click.echo('')

def space() : click.echo('')

def check_headers(json):
    required_headers = ['access_token', 'expires_in', 'refresh_expires_in', 'refresh_token', 'token_type', 'not-before-policy', 'session_state', 'scope', 'TIMESTAMP']
    for header in required_headers:
        if header not in json:
            return False
    return True

def pretty_print(json_data) : 
    print(json.dumps(json_data, indent=4))


def set_headers(token) :
    return {'Authorization': f'Bearer {token}'}


def command_with_options(prompt_message, options):
    questions = [
        inquirer.List('option',
                      message=prompt_message,
                      choices=options,
                      ),
    ]
    answer = inquirer.prompt(questions)
    return answer['option']

def format_datetime_to_json_serializable(date):
    """
    Converts a datetime object to a string in the format 'dd-mm-yyyy 00:00:00'.
    
    Args:
        dt (datetime): The datetime object to be formatted.
        
    Returns:
        str: The formatted datetime string.
    """
    return date.strftime('%d-%m-%Y 00:00:00')
    

