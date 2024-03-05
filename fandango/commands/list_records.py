
import click
from ..aria_client import AriaClient


@click.command()
def list_records():
    cli = AriaClient()
    cli.list_records()

