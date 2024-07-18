from fGOaria.utils.utility_functions import get_entity
from fGOaria.utils.imports_config import click
from fGOaria.classes.aria_client import AriaClient

@click.command()
def list_buckets():
    """Display buckets associated with a Visit or Proposal"""

    cli = AriaClient()
    entity_details = get_entity()
    manager = cli.new_cli_manager(entity_details.get('id'),entity_details.get('type'),True)
    manager.printer_cli('Bucket')