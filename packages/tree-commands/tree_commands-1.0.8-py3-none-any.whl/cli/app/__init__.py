# app/__init__.py
import click
from tree_commands import TreeCommands
import os

@click.group()
def app():
    """Your app command."""
    pass

TreeCommands.leaf(app, os.path.dirname(__file__))
