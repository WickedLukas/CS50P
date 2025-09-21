from fuel import convert, gauge

import pytest


# Convert must output correctly rounded values.
def test_convert():
    assert convert("1/100") == 1
    assert convert("1/5") == 20
    assert convert("3/5") == 60
    assert convert("99/100") == 99


# Convert must output correct minimum and maximum values.
def test_convert_limits():
    assert convert("0/2") == 0
    assert convert("3/3") == 100


# Convert must throw an exception when dividing by zero.
def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


# Convert must throw a ValueError when a wrong type is provided.
def test_convert_type():
    with pytest.raises(ValueError):
        convert("a/2")
    with pytest.raises(ValueError):
        convert("1/b")
    with pytest.raises(ValueError):
        convert("a/b")

    with pytest.raises(ValueError):
        convert("1.1/2")
    with pytest.raises(ValueError):
        convert("1/2.1")
    with pytest.raises(ValueError):
        convert("1.1/2.1")


# Convert must throw a ValueError when there is no division.
def test_convert_division():
    with pytest.raises(ValueError):
        convert("12")


# Convert must throw a ValueError when the percentage is out of range (<0 or >100).
def test_convert_range():
    with pytest.raises(ValueError):
        convert("-1/2")
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("4/3")


# Gauge must output values >0 or <100 as text with a percentage sign.
def test_gauge_percent():
    assert gauge(2) == "2%"
    assert gauge(8) == "8%"
    assert gauge(32) == "32%"
    assert gauge(65) == "65%"
    assert gauge(98) == "98%"


# Gauge must output "E" for 0 and "F" for 100.
def test_gauge_limits():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
