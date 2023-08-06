import os
import sys
import shutil

import click
import docker

from yamlflow.dockerfiles import (
    base, 
    torch_cpu, 
    APP
)


client = docker.from_env()

BASE_DIR = ".yamlflow"


def _init(docker_registry, docker_username):
    shutil.copyfile(f"{APP}/Dockerfile", f"{BASE_DIR}/Dockerfile")
    shutil.copyfile(f"requirements.txt", f"{BASE_DIR}/requirements.txt")
    shutil.copyfile(f"predictor.py", f"{BASE_DIR}/predictor.py")
    with open(f"{BASE_DIR}/config", "w") as f:
        f.write(f"registry:{docker_registry}\nusername:{docker_username}")
    client.images.build(path=base, tag="ml_model_server:base")
    client.images.build(path=torch_cpu, tag="ml_model_server:torch-cpu")


@click.command()
@click.option('--docker-registry', prompt=True)
@click.option('--docker-username', prompt=True)
def init(docker_registry, docker_username):
    """Initialize yamlflow configs"""
    click.echo(
        click.style(
            "Initializing yamlflow ...",
            fg="green"
        )
    )
    start_again = None
    try:
        os.mkdir(BASE_DIR)
    except FileExistsError as _:
        start_again = click.confirm(
            "Directory already exists, do you want to override? "
        )
    finally:
        client.images.build(path=base, tag="ml_model_server:base")
        client.images.build(path=torch_cpu, tag="ml_model_server:torch-cpu")
    

    if start_again == None:
        # pure initialization
        _init(docker_registry, docker_username)
    if start_again == True:
        # directory exists and user wants to override
        shutil.rmtree(BASE_DIR)
        os.mkdir(BASE_DIR)
        _init(docker_registry, docker_username)
    if start_again == False:
        # directory exists and user doesn't want ot override
        sys.exit(1)
    