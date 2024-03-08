
import click
from ..aria_client import AriaClient


@click.command()
def list_fields():
    cli = AriaClient()
    manager = cli.new_data_manager()
    bucket_id = manager.select_bucket()
    manager.bucket_manager.id = bucket_id
    # manager.bucket_manager.populate()
    decision = click.confirm('Would you like to narrow fields to a record?')
    record_id = None
    if decision :
        record_id = manager.select_record()
    manager.fields_manager.print_fields(record_id)

