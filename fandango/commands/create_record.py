
import click
from ..aria_client import AriaClient


@click.command()
def create_record():
    cli = AriaClient()
    cli.create_record()

