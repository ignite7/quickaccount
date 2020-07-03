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


def test_select_option():
    test = SelectOption()
    
    assert test.provider('1') == print('OK')