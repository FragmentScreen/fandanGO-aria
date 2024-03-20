from ..utils import get_entity, pretty_print, command_with_options
import click
from ..aria_client import AriaClient


@click.command()
def create_record():
    """Create a new Record for a Visit or Proposal"""
    
    cli = AriaClient()
    entity_details = get_entity()
    manager = cli.new_cli_manager(entity_details.get('id'),entity_details.get('type'),True)
    manager.create_record_cli()

        

