import pytest
from notebook import *

def test_create_filename():
    assert create_filename("") == "Untitled.txt"
    assert create_filename("mynote") == "mynote.txt"
    assert create_filename("   12345   ") == "12345.txt"

pytest.main(["-v", "--tb=line", "-rN", __file__])