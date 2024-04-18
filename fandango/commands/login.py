
import click
from ..aria_client import AriaClient
from ..utils import get_config

config = get_config()

password_default = config["LOGIN"]['ARIA']["PASSWORD"]
email_default = config["LOGIN"]['ARIA']["EMAIL"]

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