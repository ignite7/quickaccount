"""
CLI
"""

# Click
import click

# Modules
from app.services import CreateRamdonAccount
from app.services import CreateManuallyAccount


@click.command()
@click.option(
    '--random',
    '-r',
    type=click.Choice(
        ['protonmail', 'temporary_email'],
        case_sensitive=False
    ),
    help='Create random account.'
)
@click.option(
    '--custom',
    '-c',
    type=click.Choice(
        ['protonmail', 'temporary_email'],
        case_sensitive=False
    ),
    help='Create custom account.'
)
@click.option(
    '--recovery_email',
    '-e',
    prompt=True,
    help='''
    This is used to recover your account if you 
    get locked out or forget your password.
    '''
)
def cli(random, custom, recovery_email):
    if random != None:
        CreateRamdonAccount('protonmail', recovery_email)
                
    else:
        pass

if __name__ == '__main__':
    cli()