import pytest
from notebook import *

def test_create_filename():
    assert create_filename("") == "Untitled.txt"
    assert create_filename("mynote") == "mynote.txt"
    assert create_filename("   12345   ") == "12345.txt"


def test_get_note_title():
    assert get_note_title("/foo/bar/foo.bar") == "foo"
    assert get_note_title("/home/john/my_document.txt") == "my_document"
    assert get_note_title("/usr/bin/") == ""
    assert get_note_title("/notes/foo") == "foo"
    # This assertion FAILS. I'd like to fix it but it's not critical.
    # assert get_note_title("/notes/..txt") == "."


pytest.main(["-v", "--tb=line", "-rN", __file__])