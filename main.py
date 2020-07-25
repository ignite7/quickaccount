"""
CLI
"""

# Click
import click

# Modules
from app.services import CreateAccount


@click.group(
    help='Choose a provider.'
)
def cli():
    """
    Handler to group the CLI number 1.
    """

    pass


@cli.command(
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
@click.option(
    '--proxy',
    '-P',
    is_flag=True,
    default=False,
    help='Use SSL proxy.'
)
def protonmail(username, password, recovery_email, proxy):
    """
    Create protonmail account.
    """

    create = CreateAccount(proxy)
    create.get_data(
        service='protonmail',
        username=username,
        password=password,
        recovery_email=recovery_email,
        first_name=None,
        last_name=None,
        domain=None
    )


@cli.command(
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
@click.option(
    '--proxy',
    '-P',
    is_flag=True,
    default=False,
    help='Use SSL proxy.'
)
def hotmail(username, password, first_name, last_name, domain, proxy):
    """
    Create hotmail account.
    """

    create = CreateAccount(proxy)
    create.get_data(
        service='hotmail',
        username=username,
        password=password,
        recovery_email=None,
        first_name=first_name,
        last_name=last_name,
        domain=domain
    )


@cli.command(
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
@click.option(
    '--proxy',
    '-P',
    is_flag=True,
    default=False,
    help='Use SSL proxy.'
)
def fastmail(username, password, first_name, domain, proxy):
    """
    Create fastmail account.
    """

    create = CreateAccount(proxy)
    create.get_data(
        service='fastmail',
        username=username,
        password=password,
        recovery_email=None,
        first_name=first_name,
        last_name=None,
        domain=domain
    )


if __name__ == '__main__':
    cli()
