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
