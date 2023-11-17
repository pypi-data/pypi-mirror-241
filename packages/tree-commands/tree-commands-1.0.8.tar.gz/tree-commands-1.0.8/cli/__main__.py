import os
import click
from tree_commands import TreeCommands

@click.group()
def cli():
    pass

if __name__ == "__main__":
    TreeCommands.root(cli)
    cli()
