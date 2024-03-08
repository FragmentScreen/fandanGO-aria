
import click
from ..aria_client import AriaClient


@click.command()
def list_records():
    cli = AriaClient()
    manager = cli.new_data_manager()
    bucket_id = manager.select_bucket()
    manager.bucket_manager.id = bucket_id
    # manager.bucket_manager.populate()

    manager.print_records()
    
        