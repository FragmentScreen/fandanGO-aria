
import click
from ..aria_client import AriaClient
from ..utils import get_config

config = get_config()

password_default = config["login"]["PASSWORD"]
email_default = config["login"]["EMAIL"]

@click.command()
@click.option('--username', prompt='Your ARIA email address', help='Your ARIA email address', default=email_default)
@click.option('--password', prompt=True, hide_input=True, help='Your password', default='')
def login(username, password):
    """Login to ARIA and retrieve a token. Store in keyring."""
    aria_cli = AriaClient(True)
    aria_cli.login(username, password_default)
