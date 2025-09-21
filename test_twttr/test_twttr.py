from twttr import shorten

import pytest


# Test with lower case letters.
def test_shorten_lower_case():
    assert shorten("aeiou") == ""
    assert shorten("twitter") == "twttr"


# Test with upper case letters.
def test_shorten_upper_case():
    assert shorten("AEIOU") == ""
    assert shorten("TWITTER") == "TWTTR"


# Test with mixed case letters.
def test_shorten_mixed_case():
    assert shorten("aAeEiIoOuU") == ""
    assert shorten("TwItTeR") == "TwtTR"


# Test with mixed case letters and numbers.
def test_shorten_mixed_case_numbers():
    assert shorten("aA!e7EiIo4O?uU") == "!74?"
    assert shorten("T-w3ItT8e+R") == "T-w3tT8+R"


# Test with mixed case letters numbers and special characters.
def test_shorten_mixed_case_special():
    assert shorten("aA!e7EiIo4O?uU") == "!74?"
    assert shorten("T-w3ItT8e+R") == "T-w3tT8+R"
