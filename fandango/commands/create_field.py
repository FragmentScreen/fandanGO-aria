from ..utils import get_entity
import click
from ..aria_client import AriaClient


@click.command()
def create_field():
    """Create a new Fieldd for a Visit or Proposal"""

    cli = AriaClient()
    entity_details = get_entity()
    manager = cli.new_cli_manager(entity_details.get('id'),entity_details.get('type'),True)
    manager.create_field_cli()
        



