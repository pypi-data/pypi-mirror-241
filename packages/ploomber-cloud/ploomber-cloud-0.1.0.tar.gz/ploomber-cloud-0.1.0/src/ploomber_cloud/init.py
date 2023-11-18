from pathlib import Path


import click


from ploomber_cloud.exceptions import BasePloomberCloudException
from ploomber_cloud import api
from ploomber_cloud.config import PloomberCloudConfig


VALID_PROJECT_TYPES = {
    # voila is not supported yet
    "streamlit",
    "docker",
    "panel",
}


def _infer_project_type():
    """Infer project type based on the existing files in the current directory"""
    if Path("Dockerfile").exists():
        return "docker"
    else:
        return None


def _prompt_for_project_type(prefix=None):
    """Prompt the user for a project type"""
    prefix = prefix or ""
    click.echo(f"{prefix}Please specify one of: " f"{', '.join(VALID_PROJECT_TYPES)}")

    return click.prompt(
        "Project type",
        type=click.Choice(VALID_PROJECT_TYPES),
        show_choices=False,
    )


def init():
    """Initialize a project"""
    config = PloomberCloudConfig()

    if config.exists():
        raise BasePloomberCloudException(
            "Project already initialized. "
            "Run 'ploomber-cloud deploy' to deploy your project."
        )
    else:
        click.echo("Initializing new project...")

        project_type = _infer_project_type()

        if project_type is None:
            project_type = _prompt_for_project_type(
                prefix="Could not infer project type. "
            )
        else:
            click.echo(f"Inferred project type: {project_type!r}")
            correct_project_type = click.confirm("Is this correct?")

            if not correct_project_type:
                project_type = _prompt_for_project_type()

        client = api.PloomberCloudClient()
        output = client.create(project_type=project_type)
        config.dump(output)
        click.echo(f"Your app {output['id']!r} has been configured successfully!")
