# cli.py
import click

from fandango.commands.login import login
from fandango.commands.help import help
from fandango.commands.create_bucket import create_bucket
from fandango.commands.list_buckets import list_buckets
from fandango.commands.create_record import create_record
from fandango.commands.list_records import list_records
from fandango.commands.create_field import create_field
from fandango.commands.list_fields import list_fields
from fandango.commands.get_visits import get_visits

@click.group()
def cli():
    """
    💃🕺 💃🕺 💃🕺💃 🕺💃🕺 💃🕺💃 🕺💃🕺 💃🕺 💃🕺 💃🕺
    
                Welcome to Fandango

              ¿Dónde está la biblioteca 
       
    
    💃🕺 💃🕺 💃🕺💃 🕺💃 🕺💃🕺 💃🕺 💃🕺💃 🕺💃🕺 💃🕺
    """
    pass

cli.add_command(login)
cli.add_command(help)
cli.add_command(create_bucket)
cli.add_command(list_buckets)
cli.add_command(create_record)
cli.add_command(list_records)
cli.add_command(create_field)
cli.add_command(list_fields)
cli.add_command(get_visits)

if __name__ == '__main__':
    cli()
