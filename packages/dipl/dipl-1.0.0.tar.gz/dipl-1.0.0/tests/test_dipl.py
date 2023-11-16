import sys, os
import pytest
import numpy as np
sys.path.insert(0, 'src')

import dipl

def test_reading():
    
    text = """
    width float = 23.34 cm
    age int = 23 yr
    """
    assert dipl.load(text) == {
        'width': (23.34, 'cm'),
        'age': (23, 'yr')
    }

