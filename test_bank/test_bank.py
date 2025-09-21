from bank import value

import pytest


# Test "greetings" starting with "hello".
def test_startswidth_hello():
    assert value("Hello John!") == 0
    assert value("hello john") == 0


# Test "greetings" starting with "h".
def test_startswidth_h():
    assert value("Hey John!") == 20
    assert value("hey john") == 20


# Test "greetings" starting with neither "hello" nor "h".
def test_startswidth_no_hello_or_h():
    assert value("Greetings John!") == 100
    assert value("greetings john") == 100
    assert value("John, hi!") == 100
    assert value("John, hello!") == 100
