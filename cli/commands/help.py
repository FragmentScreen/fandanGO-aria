import click
from aria_data_deposition.utils import print_with_spaces

@click.command()
def help():
    """Display help information for Aria Data Deposition."""

    print_with_spaces('Welcome to the ARIA Data Deposition toolkit.')
    click.echo('----------------------------------------------')
    click.echo('Available commands:')
    click.echo('')
    click.echo(' aria-login : Login to the project and retrieve a token.')
    click.echo(' aria-get   : Test Token handling')
    click.echo(' aria-help  : Display help information.')
    print_with_spaces('')