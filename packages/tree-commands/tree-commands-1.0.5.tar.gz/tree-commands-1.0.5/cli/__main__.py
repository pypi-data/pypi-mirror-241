import click
import os
import importlib
from tree_commands import root
import pkgutil

# from cli.build import build

import sys


@click.group()
def cli():
    pass

def list_modules(directory):
    """List available modules in the specified directory."""
    modules = []
    
    # Use pkgutil.iter_modules to iterate over available modules in the directory
    for module_info in pkgutil.iter_modules([directory]):
        modules.append(module_info.name)

    return modules

def list_submodules(module):
    """List submodules inside the specified module."""
    submodules = []
    
    # Use pkgutil.iter_modules to iterate over submodules inside the module
    for submodule_info in pkgutil.iter_modules(module.__path__):
        submodules.append(submodule_info.name)

    return submodules



BASE_DIRECTORY = os.environ.get("TREE_COMMANDS_DIRECTORY", "cli")

# root(cli)
if __name__ == "__main__":
    # cli()
    # Specify the directory path
    # Specify the directory path
    directory_path = '.'

    # Get the list of available modules in the specified directory
    available_modules = list_modules(directory_path)

    # Print the list of modules and their submodules
    for module_name in available_modules:
        print(f"\nAvailable submodules in {module_name}:")
        
        # Import the module dynamically
        module = importlib.import_module(f'{directory_path}.{module_name}')
        
        # Get and print the list of submodules
        submodules = list_submodules(module)
        for submodule in submodules:
            print(f" - {submodule}")