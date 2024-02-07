
import click
from aria_data_deposition.classes.aria_client import AriaClient

@click.command()
def set_token_password():
    cli = AriaClient()
    cli.do_something()

