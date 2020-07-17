"""
CLI
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
    Create protonmail account.
    """

    create = CreateAccount()
    create.get_data(
        service='protonmail',
        username=username,
        password=password,
        recovery_email=recovery_email,
        first_name=None,
        last_name=None,
        domain=None
    )


@click.group()
def cli_custom_account():
    """
    Handler to group the CLI number 2.
    """

    pass


@cli_custom_account.command(
    help='Create hotmail account.'
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
@click.option(
    '--domain',
    '-d',
    type=click.Choice(
        ['hotmail.com', 'outlook.com'],
        case_sensitive=False
    ),
    help='Choose specific domain.'
)
def hotmail(username, password, first_name, last_name, domain):
    """
    Create hotmail account.
    """

    create = CreateAccount()
    create.get_data(
        service='hotmail',
        username=username,
        password=password,
        recovery_email=None,
        first_name=first_name,
        last_name=last_name,
        domain=domain
    )


@cli_custom_account.command(
    help='Create fastmail account.'
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
    '--domain',
    '-d',
    type=click.Choice(
        [
            'fastmail.com', 'fastmail.cn',
            'fastmail.co.uk', 'fastmail.com.au',
            'fastmail.de', 'fastmail.es',
            'fastmail.fm', 'fastmail.fr',
            'fastmail.im', 'fastmail.in',
            'fastmail.jp', 'fastmail.mx',
            'fastmail.net', 'fastmail.nl',
            'fastmail.org', 'fastmail.se',
            'fastmail.to', 'fastmail.tw',
            'fastmail.uk', 'fastmail.us'
        ],
        case_sensitive=False
    ),
    help='Choose specific domain.'
)
def fastmail(username, password, first_name, domain):
    """
    Create fastmail account.
    """

    create = CreateAccount()
    create.get_data(
        service='fastmail',
        username=username,
        password=password,
        recovery_email=None,
        first_name=first_name,
        last_name=None,
        domain=domain
    )


cli = click.CommandCollection(sources=[
    cli_random_account,
    cli_custom_account
])


if __name__ == '__main__':
    cli()
