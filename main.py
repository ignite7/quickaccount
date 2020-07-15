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
    help='Create protonmail account.'
)
@click.option(
    '--username',
    '-u',
    type=(str),
    help='Choose specific username.'
)
@click.option(
    '--password',
    '-p',
    type=(str),
    help='Choose specific password.'
)
@click.option(
    '--recovery-email',
    '-r',
    type=(str),
    help='Recover your account.'
)
def protonmail(username, password, recovery_email):
    """
    Create a random account.
    """
    
    create = CreateAccount()
    create.get_data(
        service='protonmail',
        username=username,
        password=password,
        recovery_email=recovery_email,
        first_name=None,
        last_name=None
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
    type=(str),
    help='Choose specific username.'
)
@click.option(
    '--password',
    '-p',
    type=(str),
    help='Choose specific password.'
)
@click.option(
    '--first-name',
    '-f',
    type=(str),
    help='Choose specific first name.'
)
@click.option(
    '--last-name',
    '-l',
    type=(str),
    help='Choose specific first name.'
)
def hotmail(username, password, first_name, last_name):
    """
    Create custom account.
    """
    
    create = CreateAccount()
    create.get_data(
        service='hotmail',
        username=username,
        password=password,
        recovery_email=None,
        first_name=first_name,
        last_name=last_name
    )


cli = click.CommandCollection(sources=[
    cli_random_account,
    cli_custom_account
])


if __name__ == '__main__':
    cli()