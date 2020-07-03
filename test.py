"""
Test

Note:
For capture the input and output try:
python3 -m pytest --capture=tee-sys test.py
"""

# Pytest
import pytest

# Libraries
from cli import *


def test_create_options():
    assert create_options() == '1' or create_options() == '2'