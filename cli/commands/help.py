import click

@click.command()
def help():
    """Display help information for Aria Data Deposition."""
    click.echo("Welcome to the Aria Data Deposition toolkit!")
    click.echo("Available commands:")
    click.echo("  aria-login : Login to the project and retrieve a token.")
    click.echo("  aria-another-command : Description of another command.")
    click.echo("  aria-help : Display help information.")