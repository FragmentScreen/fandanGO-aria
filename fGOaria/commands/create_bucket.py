from fGOaria.utils.utility_functions import get_entity
from fGOaria.utils.imports_config import click
from fGOaria.classes.aria_manager import ARIA

@click.command()
def create_bucket():
    """Create a new Bucket for a Visit or Proposal"""
    cli = ARIA()
    entity_details = get_entity()
    manager = cli.new_cli_manager(entity_details['id'],entity_details['type'],True)
    manager.create_bucket_cli()
