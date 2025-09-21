import pytest

from numb3rs import validate


# Check if it matches on more than requested.
def test_validate_all():
    assert validate("12.1.234.45") == True
    assert validate("127.0.0.1") == True
    assert validate("    12.1.234.45  ") == False
    assert validate("    12.1.234.45  \n") == False
    assert validate("IP: 12.1.234.45") == False
    assert validate("IP:12.1.234.45") == False
    assert validate("12.1.234.45. It is ... ") == False
    assert validate("[12.1.234.45]") == False


# Check for wrong number of periods.
def test_validate_periods():
    assert validate("12.1.234.45.210") == False
    assert validate("12") == False
    assert validate("12.1.234") == False
    assert validate(".12.1.234.45") == False
    assert validate("12.1.234.45.") == False
    assert validate(".12.1.234.45.") == False
    assert validate("12.1..45") == False


# Check for wrong character types.
def test_validate_type():
    assert validate("aaa.aaa.aaa.aaa") == False
    assert validate("12.b.234.45") == False
    assert validate("12.1.2c4.45") == False
    assert validate("12.#.234.45") == False
    assert validate("12.1.2_4.45") == False


# Check for wrong number range.
def test_validate_range():
    assert validate("12.1.234.45") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("000.000.000.000") == False
    assert validate("111.010.001.110") == False
    assert validate("-1.-1.-1.-1") == False
    assert validate("12.-1.234.45") == False
    assert validate("256.256.256.256") == False
    assert validate("12.1.256.45") == False
    assert validate('300.1.2.3') == False
    assert validate('127.300.2.3') == False
    assert validate('127.1.300.3') == False
    assert validate('127.1.2.300') == False
    assert validate('127.300.300.300') == False
