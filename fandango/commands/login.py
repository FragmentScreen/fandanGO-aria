
import click
from ..aria_client import AriaClient


@click.command()
@click.option('--username', prompt='Your ARIA email address', help='Your ARIA email address', default='lui.holliday@instruct-eric.org')
@click.option('--password', prompt=True, hide_input=True, help='Your password', default='4XSzzUq9SCe2#vkT')
def login(username, password):
    """Login to ARIA and retrieve a token. Store in keyring."""
    aria_cli = AriaClient(True)
    aria_cli.login(username, password)
