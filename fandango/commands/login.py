
import click
from ..aria_client import AriaClient
import yaml
import os
root_project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
config_path = os.path.join(root_project_dir, "../config.yml")
with open(config_path, "r") as f:
    config = yaml.safe_load(f)
password_default = config["login"]["PASSWORD"]

@click.command()
@click.option('--username', prompt='Your ARIA email address', help='Your ARIA email address', default='lui.holliday@instruct-eric.org')
@click.option('--password', prompt=True, hide_input=True, help='Your password', default='')
def login(username, password):
    """Login to ARIA and retrieve a token. Store in keyring."""
    aria_cli = AriaClient(True)
    aria_cli.login(username, password_default)
