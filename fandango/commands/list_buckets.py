
import click
from ..aria_client import AriaClient


@click.command()
def list_buckets():
    cli = AriaClient()
    cli.list_buckets()

