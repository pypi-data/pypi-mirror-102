import os
import sys
import shutil

import click
import docker

client = docker.from_env()


@click.command()
@click.option('--registry', prompt=True)
@click.option('--username', prompt=True)
def init(registry, username):
    """Initialize yamlflow configs"""
    click.echo(
        click.style(
            "Initializing yamlflow ...",
            fg="green"
        )
    )
    base_dir = ".yamlflow"
    try:
        os.makedirs(base_dir)
    except FileExistsError as _:
        continue_ = click.confirm("Directory already exists, do you want to override? ")
        shutil.rmtree(base_dir) if  continue_ else sys.exit(1)
    # at this point we'are sure no config exists, so let's create from scratch
    with open(f"{base_dir}/config", "w") as f:
        f.write(f"registry:{registry}\nusername:{username}")