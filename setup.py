"""
Setup
"""

# Setup
from setuptools import setup


setup(
    name='quickaccount',
    version='0.1',
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