from fGOaria.utils.imports_config import click
from fGOaria.commands.login import login
from fGOaria.commands.create_bucket import create_bucket
from fGOaria.commands.create_record import create_record
from fGOaria.commands.create_field import create_field
from fGOaria.commands.list_buckets import list_buckets
from fGOaria.commands.list_records import list_records
from fGOaria.commands.list_fields import list_fields


@click.group()
def cli():
    """
    💃🕺 💃🕺 💃🕺💃 🕺💃🕺 💃🕺💃 🕺💃🕺 💃🕺 💃🕺 💃🕺
    
                Welcome to fandanGO-aria
       
    
    💃🕺 💃🕺 💃🕺💃 🕺💃 🕺💃🕺 💃🕺 💃🕺💃 🕺💃🕺 💃🕺
    """
    pass

cli.add_command(login)
cli.add_command(create_bucket)
cli.add_command(create_record)
cli.add_command(create_field)
cli.add_command(list_buckets)
cli.add_command(list_records)
cli.add_command(list_fields)

if __name__ == '__main__':
    cli()