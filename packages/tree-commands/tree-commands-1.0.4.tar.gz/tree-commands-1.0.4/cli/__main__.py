import click
import os
import importlib
from tree_commands import root

import sys

@click.group()
def cli():
    pass

BASE_DIRECTORY = os.environ.get("TREE_COMMANDS_DIRECTORY", "cli")

# root(cli)
if __name__ == "__main__":
    cli()
