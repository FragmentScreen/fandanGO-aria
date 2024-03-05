
import click
from ..aria_client import AriaClient


@click.command()
def create_field():
    cli = AriaClient()
    cli.create_field()

