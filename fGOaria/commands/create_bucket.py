from fGOaria.utils.utility_functions import get_entity
from fGOaria.utils.imports_config import click
from fGOaria.classes.aria_client import AriaClient

@click.command()
def create_bucket():
    """Create a new Bucket for a Visit or Proposal"""
    cli = AriaClient()
    entity_details = get_entity()
    manager = cli.new_cli_manager(entity_details.get('id'),entity_details.get('type'),True)
    manager.create_bucket_cli()
