from fGOaria.utils.utility_functions import get_entity
from fGOaria.utils.imports_config import click
from fGOaria.classes.aria_client import AriaClient


@click.command()
def tech_eval():

    cli = AriaClient()
    tech = cli.new_cli_tech_eval()
    tech.menu()
