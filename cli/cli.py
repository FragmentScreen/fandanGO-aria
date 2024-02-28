# cli.py
import click
from cli.commands.login import login
from cli.commands.help import help
from cli.commands.create_bucket import create_bucket
from cli.commands.list_buckets import list_buckets
from cli.commands.create_record import create_record
from cli.commands.list_records import list_records
from cli.commands.create_field import create_field
from cli.commands.list_fields import list_fields
from cli.commands.get_visits import get_visits
from aria_data_deposition.classes.aria_client import AriaClient

@click.group()
def cli():
    """Aria Data Deposition CLI."""
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
