
import click
from ..aria_client import AriaClient


@click.command()
def create_field():
    cli = AriaClient()
    manager = cli.new_data_manager()

    exisiting_bucket = click.confirm('Create field for existing bucket?', default='n')
    exisiting_record = False
    if not exisiting_bucket :
        click.echo('Creating new Bucket...')
        bucket_id = manager.create_bucket()
        click.echo('Creating new Record...')
        record_id = manager.create_record()
    else:
        bucket_id = manager.select_bucket()
        manager.bucket_manager.id = bucket_id
        # manager.bucket_manager.populate()
        exisiting_record = click.confirm('Create field for existing record?', default='n')
        if not exisiting_record :
            click.echo('Creating new Record...')
            record_id = manager.create_record()
        else :
            print(manager.records_manager.records)
            record_id = manager.select_record()
    
    manager.create_field(record_id)
    manager.print_bucket_info()
        



