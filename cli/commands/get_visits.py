
import click
from aria_data_deposition.classes.aria_client import AriaClient

@click.command()
@click.option('--vid', prompt='VID Filter', help='Filter to a specific Visit', default='optional')
def get_visits(vid):
    vid = None if vid == 'optional' else vid
    cli = AriaClient()
    cli.get_visits(vid)

