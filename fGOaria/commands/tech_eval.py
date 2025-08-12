from fGOaria.utils.utility_functions import get_entity
from fGOaria.utils.imports_config import click
from fGOaria.classes.aria_manager import ARIA


@click.command()
def tech_eval():
    """Retrieve & Submit Technical Review for a Visit"""

    cli = ARIA()
    tech = cli.new_cli_tech_eval()
    tech.menu()
