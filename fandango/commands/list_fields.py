
import click
from ..aria_client import AriaClient


@click.command()
def list_fields():
    cli = AriaClient()
    cli.list_fields()

