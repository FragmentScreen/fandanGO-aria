
import click
from aria_data_deposition.classes.aria_client import AriaClient

@click.command()
@click.option('--username', prompt='Your ARIA email address', help='Your ARIA email address', default='aria.test.admin@instruct-eric.eu')
@click.option('--password', prompt=True, hide_input=True, help='Your password', default='')
def login(username, password):
    """Login to ARIA and retrieve a token. Store in keyring."""
    aria_cli = AriaClient()
    aria_cli.login(username, password)
