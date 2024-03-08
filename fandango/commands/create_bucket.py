
import click
from ..aria_client import AriaClient

@click.command()
def create_bucket():
    cli = AriaClient()
    microscopy = cli.new_data_manager()
    microscopy.create_bucket()
    microscopy.print_bucket_info()


