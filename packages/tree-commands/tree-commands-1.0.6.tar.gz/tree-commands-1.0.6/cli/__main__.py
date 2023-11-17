import click
import os
import importlib
from tree_commands import TreeCommands
import pkgutil

# from cli.build import build

import sys


@click.group()
def cli():
    pass
    
BASE_DIRECTORY = os.environ.get("TREE_COMMANDS_DIRECTORY", "cli")
def root(group: click.Group):
    for file_name in os.listdir(BASE_DIRECTORY):
        if os.path.isdir(
            os.path.join(BASE_DIRECTORY, file_name)
        ) and not file_name.startswith("__"):
            module_path = f"{BASE_DIRECTORY}.{file_name}.__init__"
            command = getattr(importlib.import_module(module_path), file_name)
            group.add_command(command)
            try:
                command_module = importlib.import_module(module_path)
                group.add_command(getattr(command_module, file_name))
            except ModuleNotFoundError as e:
                print(f"Error importing module {module_path}: {e}")


if __name__ == '__main__':
    root(cli)
    cli()
