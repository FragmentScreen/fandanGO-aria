# cli.py
import click
from cli.commands.login import login
from cli.commands.help import help
from cli.commands.get_visits import get_visits
from aria_data_deposition.classes.aria_client import AriaClient

@click.group()
def cli():
    """Aria Data Deposition CLI."""
    pass




cli.add_command(login)
cli.add_command(help)
cli.add_command(get_visits)

if __name__ == '__main__':
    cli()
