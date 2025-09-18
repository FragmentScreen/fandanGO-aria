from fGOaria.utils.utility_functions import get_entity
from fGOaria.utils.imports_config import click
from fGOaria.classes.aria_manager import ARIA

@click.command()
def create_bucket():
    """Create a new Bucket for a Visit or Proposal"""
    cli = ARIA()
    entity_details = get_entity()
    manager = cli.new_cli_data_manager(entity_details['id'], entity_details['type'], True)
    manager.create_bucket_cli()

@click.command()
def list_buckets():
    """Display buckets associated with a Visit or Proposal"""
    cli = ARIA()
    entity_details = get_entity()
    manager = cli.new_cli_data_manager(entity_details.get('id'), entity_details.get('type'), True)
    manager.printer_cli('Bucket')

@click.command()
def create_record():
    """Create a new Record for a Visit or Proposal"""
    cli = ARIA()
    entity_details = get_entity()
    manager = cli.new_cli_data_manager(entity_details.get('id'), entity_details.get('type'), True)
    manager.create_record_cli()

@click.command()
def list_records():
    """Display fields associated with a Visit or Proposal"""
    cli = ARIA()
    entity_details = get_entity()
    manager = cli.new_cli_data_manager(entity_details.get('id'), entity_details.get('type'), True)
    manager.printer_cli('Record')

@click.command()
def create_field():
    """Create a new Fieldd for a Visit or Proposal"""
    cli = ARIA()
    entity_details = get_entity()
    manager = cli.new_cli_data_manager(entity_details.get('id'), entity_details.get('type'), True)
    manager.create_field_cli()

@click.command()
def list_fields():
    """Display records associated with a Visit or Proposal"""
    cli = ARIA()
    entity_details = get_entity()
    manager = cli.new_cli_data_manager(entity_details.get('id'), entity_details.get('type'), True)
    manager.printer_cli('Field')