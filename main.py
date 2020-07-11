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
def random():
    """
    Create a random account.
    """
    
    create = CreateAccount()
    create.create_data(
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
def custom(username, password):
    """
    Create custom account.
    """
    
    create = CreateAccount()
    create.create_data(username, password)


cli = click.CommandCollection(sources=[
    cli_random_account,
    cli_custom_account
])


if __name__ == '__main__':
    cli()