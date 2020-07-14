"""
CLI
pip3 install --editable .
"""

# Click
import click

# Modules
from app.services import CreateAccount


@click.group()
def cli_random_account():
    """
    Handler to group the CLI number 1.
    """ 
     
    pass


@cli_random_account.command(
    help='Create random account.'
)
@click.option(
    '--service',
    '-s',
    type=click.Choice(
        [
            'protonmail',
            'hotmail'
        ],
        case_sensitive=False
    ),
    required=True,
    help='Choose the service to make an account.'
)
def random(service):
    """
    Create a random account.
    """
    
    create = CreateAccount()
    create.get_data(
        service=service,
        username=None,
        password=None
    )


@click.group()
def cli_custom_account():
    """
    Handler to group the CLI number 2.
    """ 
     
    pass


@cli_custom_account.command(
    help='Create custom account.'
)
@click.option(
    '--service',
    '-s',
    type=click.Choice(
        [
            'protonmail',
            'hotmail'
        ],
        case_sensitive=False
    ),
    required=True,
    help='Choose the service to make an account.'
)
@click.option(
    '--username',
    '-u',
    required=True,
    help='Use a custom username.'
)
@click.option(
    '--password',
    '-p',
    required=True,
    help='Use a custom password.'
)
def custom(service, username, password):
    """
    Create custom account.
    """
    
    create = CreateAccount()
    create.get_data(service, username, password)


cli = click.CommandCollection(sources=[
    cli_random_account,
    cli_custom_account
])


if __name__ == '__main__':
    cli()