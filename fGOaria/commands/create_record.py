from fGOaria.utils.utility_functions import get_entity
from fGOaria.utils.imports_config import click
from fGOaria.classes.aria_manager import ARIA

@click.command()
def create_record():
    """Create a new Record for a Visit or Proposal"""

    cli = ARIA()
    entity_details = get_entity()
    manager = cli.new_cli_manager(entity_details.get('id'),entity_details.get('type'),True)
    manager.create_record_cli()