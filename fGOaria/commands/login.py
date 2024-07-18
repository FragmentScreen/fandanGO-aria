from fGOaria.utils.utility_functions import get_entity
from fGOaria.utils.imports_config import click, os
from fGOaria.classes.aria_client import AriaClient
from dotenv import load_dotenv

load_dotenv()

password_default = os.getenv('ARIA_CONNECTION_PASSWORD')
email_default = os.getenv('ARIA_CONNECTION_USERNAME')

if password_default :
    password_default_prompt = 'Press Enter for password stored in CONFIG.'
else :
    password_default_prompt = ''

@click.command()
@click.option('--username', prompt='Your ARIA email address', help='Your ARIA email address', default=email_default)
@click.option('--password', prompt=True, hide_input=True, help='Your password', default=password_default_prompt)
def login(username, password):
    """Login to ARIA and retrieve a token. Store in keyring."""

    if password_default_prompt == password :
        aria_cli = AriaClient(True)
        aria_cli.login(username, password_default)
    else :
        aria_cli = AriaClient(True)
        aria_cli.login(username, password)
