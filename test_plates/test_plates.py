from plates import is_valid

import pytest


# The length must be between 2 and 6 characters.
def test_is_valid_length():
    assert is_valid("ABCD12") == True
    assert is_valid("AB12") == True
    assert is_valid("ABCD123") == False
    assert is_valid("A") == False
    assert is_valid("") == False


# The first two characters must be alphabetic.
def tecst_is_valid_start():
    assert is_valid("AB") == True
    assert is_valid("3B") == False
    assert is_valid("A7") == False
    assert is_valid("37") == False
    assert is_valid("3BCD12") == False
    assert is_valid("A7CD12") == False
    assert is_valid("37CD12") == False


# The decimal number positions must be valid.
def test_is_valid_nums():
    assert is_valid("AB1") == True
    assert is_valid("AB1234") == True
    assert is_valid("ABC234") == True
    assert is_valid("AB12CD") == False
    assert is_valid("ABCD01") == False
    assert is_valid("AB0123") == False


# Characters must all be alphanumeric.
def test_is_valid_chars():
    assert is_valid("AbCd12") == True
    assert is_valid("%BCD12") == False
    assert is_valid("AB&D12") == False
    assert is_valid("ABCD-2") == False
