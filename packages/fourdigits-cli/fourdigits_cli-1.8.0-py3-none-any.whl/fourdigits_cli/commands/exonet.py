import os

import click
import requests

from fourdigits_cli.settings import DEFAULT_CONFIG

DRONE_BUILD_URL = os.getenv(
    "DRONE_BUILD_URL",
    "https://drone.exonet.nl/api/repos/exonet/containers-fourdigits/builds",
)


@click.group()
def group():
    pass


@group.command()
@click.argument("environment")
@click.argument("docker_tag")
@click.option("--message", default="", show_default=True)
def deploy(environment, docker_tag, message=""):
    drone_token = os.getenv("DRONE_TOKEN", "")
    if not drone_token:
        raise click.ClickException("Environment variable DRONE_TOKEN is not set")

    if environment not in DEFAULT_CONFIG.environments:
        raise click.ClickException("Environment doesn't exists in the pyproject.toml")

    if not DEFAULT_CONFIG.exonet_project_name:
        raise click.ClickException(
            "The option exonet_project_name doesn't exists in the pyproject.toml"
        )

    if not message:
        message = f"[{DEFAULT_CONFIG.exonet_project_name}] Deploying {docker_tag} to {environment} environment"  # noqa: E501

    response = requests.post(
        url=DRONE_BUILD_URL,
        headers={
            "Authorization": f"Bearer {drone_token}",
        },
        params={
            "name": DEFAULT_CONFIG.exonet_project_name,
            "target": environment,
            "tag": docker_tag,
            "slack_channel": DEFAULT_CONFIG.slack_channel,
            "message": message,
        },
    )

    if response.status_code != 200:
        raise click.ClickException(response.text)
    click.echo(response.text)
