# cli.py
import click
from cli.commands.login import login
from cli.commands.help import help
from cli.commands.get_token_password import get_token_password
from aria_data_deposition.classes.aria_client import AriaClient

@click.group()
def cli():
    """Aria Data Deposition CLI."""
    pass


aria_client_instance = AriaClient()

cli.add_command(login)
cli.add_command(help)
cli.add_command(get_token_password)

if __name__ == '__main__':
    cli()
