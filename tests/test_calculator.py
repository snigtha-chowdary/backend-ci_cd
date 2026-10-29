"""import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)"""

from calculator import *

def test_add():
    assert add(10,20)==30

def test_subtract():
    assert subtract(20,10)==10

def test_multiply():
    assert multiply(4,5)==20

def test_divide():
    assert divide(20,4)==5
