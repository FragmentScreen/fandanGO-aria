
import click
from aria_data_deposition.classes.aria_client import AriaClient

@click.command()
@click.option('--username', prompt='Your username', help='Your username')
@click.option('--password', prompt=True, hide_input=True, help='Your password')
def login(username, password):
    """Login to the project and retrieve a token."""
    AriaClient.login(username, password)
