import click

from yamlflow import __version__

@click.command()
def version():
    """Version of yamlflow"""
    click.echo(click.style(f"yamlflow:{__version__}", fg="green"))
