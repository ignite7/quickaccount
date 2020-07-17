"""
Setup
"""

# Libraries
from setuptools import setup


setup(
    author='Sergio van Berkel',
    name='quickaccount',
    version='0.1v',
    py_modules=['main'],
    install_requires=[
        'click',
        'selenium'
    ],
    entry_points='''
        [console_scripts]
        quickaccount=main:cli
    ''',
)