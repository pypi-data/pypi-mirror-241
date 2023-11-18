import click

from ploomber_cloud import api_key, deploy as deploy_, init as init_


@click.group()
def cli():
    pass


@cli.command()
@click.argument("key", type=str, required=True)
def key(key):
    """Set your API key"""
    api_key.set_api_key(key)


@cli.command()
def deploy():
    """Deploy your project to Ploomber Cloud"""
    deploy_.deploy()


@cli.command()
def init():
    """Initialize a Ploomber Cloud project"""
    init_.init()


if __name__ == "__main__":
    cli()
