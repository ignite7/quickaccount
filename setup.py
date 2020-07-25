"""
Setup
"""

# Libraries
from setuptools import setup, find_packages
from os import path, system

# Adsolute path
here = path.abspath(path.dirname(__file__))

# Requires
install_requires_file = open(
    path.join(here, 'requirements.txt'),
    'r+'
).read().splitlines()

# Long description from README.md file
with open(path.join(here, 'README.md'), encoding = 'utf-8') as readme:
    long_description = readme.read()

# Specifications of the setup
setup(
    name = 'quickaccount',
    version = '0.1v',
    description = 'Create quick account!',
    long_description = long_description,
    url = 'https://www.sergiovanberkel.com/',
    author = 'Sergio van Berkel Acosta',
    author_mail = 'sergio.vanberkel@gmail.com',
    python_requires = '>=3.6.*',
    install_requires = install_requires_file or system(
        'pip install -r ./requirements.txt'
    ),
    packages = find_packages(),
    py_modules=['main'],
    entry_points='''
        [console_scripts]
        quickaccount=main:cli
    '''
)