"""
CLI
pip3 install --editable .
"""

# Click
import click

# Modules
from app.services import CreateRamdonAccount
from app.services import CreateCustomAccount


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
    
    CreateRamdonAccount()


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
@click.option(
    '--recovery_email',
    '-r',
    help='Recover your account if you lose the password.'
)
def custom(username, password, recovery_email):
    """
    Create custom account.
    """
    
    CreateCustomAccount(username, password, recovery_email)


cli = click.CommandCollection(sources=[
    cli_random_account,
    cli_custom_account
])


if __name__ == '__main__':
    cli()