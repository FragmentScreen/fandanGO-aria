import warnings
warnings.filterwarnings("ignore")

from fGOaria.utils.imports_config import click
from fGOaria.commands.login import login
from fGOaria.commands import data
from fGOaria.commands import visit


@click.group()
def cli():
    """
    💃🕺 💃🕺 💃🕺💃 🕺💃🕺 💃🕺💃 🕺💃🕺 💃🕺 💃🕺 💃🕺 💃🕺

         Welcome to the fandanGO-aria demonstration tool

    💃🕺 💃🕺 💃🕺💃 🕺💃 🕺💃🕺 💃🕺 💃🕺💃 🕺💃🕺 💃🕺 💃🕺
    """
    pass

cli.add_command(login)
cli.add_command(data.create_bucket, 'create-bucket')
cli.add_command(data.create_record, 'create-record')
cli.add_command(data.create_field, 'create-field')
cli.add_command(data.list_buckets, 'list-buckets')
cli.add_command(data.list_records, 'list-records')
cli.add_command(data.list_fields, 'list-fields')
cli.add_command(visit.tech_eval, 'tech-eval')

if __name__ == '__main__':
    cli()