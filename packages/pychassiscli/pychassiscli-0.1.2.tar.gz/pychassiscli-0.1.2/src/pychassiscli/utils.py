import os
import shutil
from contextlib import contextmanager

from mako.template import Template
from rich import print as rich_print
from python_on_whales import DockerException, ClientNotFoundError, DockerClient


def check_docker():
    """
    Check if docker and docker compose are installed and running.
    """
    docker = DockerClient()
    try:
        docker.ps()
    except ClientNotFoundError:
        rich_print('Please install docker firstly')
        raise
    except DockerException:
        rich_print('Please start docker correctly')
        raise

    rich_print('[bold magenta]Docker is installed successfully[/bold magenta]', ":vampire:")

    if not docker.compose.is_installed():
        rich_print('Please install docker compose firstly')
        raise

    rich_print('[bold magenta]Docker Compose is installed successfully[/bold magenta]', ":vampire:")


@contextmanager
def status(status_msg: str, newline: bool = False, quiet: bool = False):
    """
    Show status message and yield.
    """
    msg_suffix = ' ...' if not newline else ' ...\n'
    rich_print(status_msg + msg_suffix)
    try:
        yield
    except Exception as e:
        if not quiet:
            rich_print('  [bold magenta]FAILED[/bold magenta]\n')
        raise
    else:
        if not quiet:
            rich_print('  [bold magenta]Done[/bold magenta]\n')


def get_directory(dir_name: str) -> str:
    """
    Return the directory path of the given pychassiscli directory name.
    """
    import pychassiscli

    package_dir = os.path.abspath(os.path.dirname(pychassiscli.__file__))
    return os.path.join(package_dir, dir_name)


def copy_files(src_dir, dest_dir):
    for file_ in os.listdir(src_dir):
        if file_ == '__pycache__':
            continue

        src_file_path = os.path.join(src_dir, file_)
        output_file = os.path.join(dest_dir, file_)
        if os.path.isdir(src_file_path):
            copy_files(src_file_path, output_file)
        else:
            with status(f'Generating {os.path.abspath(output_file)}'):
                shutil.copy(src_file_path, output_file)


def template_to_file(
        template_file: str, dest: str, output_encoding: str, **kw
) -> None:
    template = Template(filename=template_file)
    try:
        output = template.render_unicode(**kw).encode(output_encoding)
    except Exception as e:
        rich_print('Template rendering failed.')
        raise
    else:
        with open(dest, "wb") as f:
            f.write(output)


if __name__ == '__main__':
    with status(f'Generating Test'):
        pass