from jar import Jar

import pytest


def test_init():
    """
    Test if the jar is initialized correctly with positive capacities
    and ValueError is raised for negative capacities.
    """
    assert Jar().capacity == 12
    assert Jar(0).capacity == 0
    assert Jar(1).capacity == 1
    assert Jar(12).capacity == 12
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar(-12)


def test_deposit():
    """
    Test if depositing into the jar works correctly and
    ValueError is raised when the capacity would be exceeded or
    for negative values.
    """
    jar = Jar(20)
    jar.deposit(0)
    assert jar.size == 0
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(15)
    assert jar.size == 16
    jar.deposit(4)
    assert jar.size == 20
    with pytest.raises(ValueError):
        jar.deposit(1)
    with pytest.raises(ValueError):
        jar.deposit(-1)


def test_withdraw():
    """
    Test if withdrawing from the jar works correctly and
    ValueError is raised when the there are not enough cookies or
    for negative values.
    """
    jar = Jar(20)
    jar.deposit(20)
    assert jar.size == 20
    jar.withdraw(1)
    assert jar.size == 19
    jar.withdraw(15)
    assert jar.size == 4
    jar.withdraw(4)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(1)
    with pytest.raises(ValueError):
        jar.withdraw(-1)


def test_str():
    """
    Test if the correct number of emojis are printed
    representing the number of cookies.
    """
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
