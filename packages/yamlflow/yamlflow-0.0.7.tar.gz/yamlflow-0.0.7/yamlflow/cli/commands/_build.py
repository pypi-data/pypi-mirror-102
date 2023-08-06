import shutil

import click
import docker

from yamlflow.cli.constants import BASE_DIR
from yamlflow.cli.manifest import Manifest

client = docker.from_env()


@click.command()
@click.option('-f', '--file', 'f', required=True)
def build(f):
    """Given a manifest file or directory containing flow.yaml, command creates a docker image"""
    manifest = Manifest(f)
    #TODO; ignore patterns should be added
    shutil.copytree("models", f"{BASE_DIR}/models")
    shutil.copytree("service", f"{BASE_DIR}/service")
    build_info = manifest.build_info()
    click.echo(
        click.style(
            f"""
            Building image ....
            Service: {build_info["tag"]}
            Backend: {build_info["buildargs"]["BACKEND"]}
            """,
            fg="blue"
        )
    )
    client.images.build(**build_info, rm=True)
    shutil.rmtree(f"{BASE_DIR}/models")
    shutil.rmtree(f"{BASE_DIR}/service")
