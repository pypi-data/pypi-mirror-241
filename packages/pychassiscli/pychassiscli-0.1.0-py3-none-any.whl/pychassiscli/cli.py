import os

import click
from rich import print as rich_print

from utils import get_directory, status, copy_files

INIT_TYPE_CHOICES = ['apiflask', 'nameko']


@click.group()
def cli():
    pass


@cli.command()
@click.option('-d', '--directory',
              default='.',
              show_default=True,
              required=True,
              help='The directory name for the template to be placed')
@click.option('-t', '--type', '_type',
              default='nameko',
              show_default=True,
              type=click.Choice(INIT_TYPE_CHOICES, case_sensitive=False),
              help='The types of the template')
def init(directory, _type):
    """
    Initialize a project via templates.
    """
    template_dir = os.path.join(get_directory('templates'), _type)
    if not os.access(template_dir, os.F_OK):
        rich_print('No such template type {}'.format(_type))
        return

    if directory != '.':
        if os.access(directory, os.F_OK) and os.listdir(directory):
            rich_print('Directory {} already exists and is not empty'.format(directory))
            return

        if not os.access(directory, os.F_OK):
            with status(f'Creating directory {os.path.abspath(directory)!r}'):
                os.makedirs(directory)

    copy_files(template_dir, directory)


if __name__ == '__main__':
    cli()
