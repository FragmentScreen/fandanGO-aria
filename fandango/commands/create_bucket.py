
import click
from ..aria_client import AriaClient

@click.command()
def create_bucket():
    cli = AriaClient()
    cli.create_bucket()

