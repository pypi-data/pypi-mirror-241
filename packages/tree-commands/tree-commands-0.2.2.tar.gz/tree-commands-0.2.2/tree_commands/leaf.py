import inspect
import os
import click
import importlib

BASE_DIRECTORY = os.environ.get("TREE_COMMANDS_DIRECTORY", "cli")


def leaf(group: click.Group):
    caller_directory = inspect.stack()[1].filename[:-12]
    for file_name in os.listdir(caller_directory):
        if file_name.endswith(".py") and file_name != "__init__.py":
            module_name = file_name[:-3]
            package_name = f"{BASE_DIRECTORY}.{caller_directory.split('/').pop()}"
            module_path = f"{package_name}.{module_name}"

            try:
                command_module = importlib.import_module(module_path)
                group.add_command(getattr(command_module, module_name))
            except ModuleNotFoundError as e:
                print(f"Error importing module {module_path}: {e}")
