import sys, os
import pytest
import numpy as np
sys.path.insert(0, 'src')

import dipl
from dipl import Format
from scinumtools.units import Quantity

def test_loading():
    
    text = """
    width float = 23.34 cm
    age int = 23 yr
      !tags ["body"]
    """
    
    assert dipl.load(text) == {
        'width': (23.34, 'cm'),
        'age': (23, 'yr')
    }

    assert dipl.load(text, Format.VALUE) == {
        'width': 23.34,
        'age': 23,
    }
    
    assert dipl.load(text, query="width") == {
        'width': (23.34, 'cm'),
    }

    assert dipl.load(text, tags=["body"]) == {
        'age': (23, 'yr'),
    }

def test_dumping():
    
    data = {
        'body': {
            'width': Quantity(172.34, 'cm'),
            'age': (23, 'yr'),
        },
        'married': True,
        'name': "John",
        'kids': ["Alice","Williams"],
        'lucky_numbers': np.array([23, 34, 5]),
    }
    
    assert dipl.dump(data) == """
body
  width float = 172.34 cm
  age int = 23 yr
married bool = true
name str = "John"
kids str[2] = ["Alice","Williams"]
lucky_numbers int[3] = [23,34,5]
    """.strip()