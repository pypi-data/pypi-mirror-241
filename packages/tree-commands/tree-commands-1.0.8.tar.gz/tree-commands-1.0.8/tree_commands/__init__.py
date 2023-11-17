# tree_commands/__init__.py
import os
import click
import importlib

class TreeCommands:
    @staticmethod
    def leaf(group: click.Group, directory: str):
        for entry in os.scandir(directory):
            if entry.name.startswith("__"):
                continue

            if entry.is_dir():
                module_path = f"{directory}.{entry.name}.__init__"
            elif entry.name.endswith(".py"):
                module_path = f"{directory}.{os.path.splitext(entry.name)[0]}"
            else:
                continue

            try:
                module = importlib.import_module(module_path)
                for obj_name in dir(module):
                    obj = getattr(module, obj_name)
                    if isinstance(obj, click.Command):
                        group.add_command(obj)

            except (ModuleNotFoundError, AttributeError) as e:
                print(f"Error importing module {module_path}: {e}")

    @staticmethod
    def root(group: click.Group):
        for file_name in os.listdir(os.path.dirname(__file__)):
            if file_name.startswith("__") or not os.path.isdir(os.path.join(os.path.dirname(__file__), file_name)):
                continue

            module_path = f"{file_name}.__init__"
            try:
                command_module = importlib.import_module(module_path)
                command_name = getattr(command_module, 'command_name', file_name)
                command = getattr(command_module, command_name)
                group.add_command(command, name=command_name)

            except (ModuleNotFoundError, AttributeError) as e:
                print(f"Error importing module {module_path}: {e}")
