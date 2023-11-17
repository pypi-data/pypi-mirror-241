import click

@click.command()
def subcommand1():
    """Subcommand 1."""
    click.echo("Executing subcommand 1.")