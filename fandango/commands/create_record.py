
import click
from ..aria_client import AriaClient


@click.command()
def create_record():
    cli = AriaClient()
    manager = cli.new_data_manager()

    exisiting_bucket = click.confirm('Create record for existing bucket?', default='n')
    if not exisiting_bucket :
        click.echo('Creating new Bucket...')
        manager.create_bucket()
        manager.create_record()
    else:
        id = manager.select_bucket()
        manager.bucket_manager.id = id
        manager.create_record()
        manager.print_bucket_info()
        

