import click
from datetime import datetime

def get_formatted_datetime(input_datetime=None, format_str='%Y-%m-%d %H:%M:%S'):
    if input_datetime is None:
        input_datetime = datetime.now()

    formatted_datetime = input_datetime.strftime(format_str)
    return formatted_datetime

def print_with_spaces(str) :
    click.echo('')
    click.echo(str)
    click.echo('')
