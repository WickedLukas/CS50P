import pytest

from um import count


# Count "um" seperated by space.
def test_count_space():
    assert count("word um word um word um word") == 3
    assert count("word UM word Um word uM word") == 3
    assert count("word um word um um word word um um um word") == 6
    assert count("word UM word Um uM word word UM Um uM word") == 6


# Count "um" seperated by different characters
def test_count_sep():
    assert count("word,um word, um, word.um?word!um word") == 4


# Count "um" when it is also at the beginning and/or end of the text.
def test_count_start_end():
    assert count("um word") == 1
    assert count("um word um") == 2
    assert count("um word um word um") == 3


# Count "um" while ignoring it when it is part of another word.
def test_count_start_end():
    assert count("um wordum word") == 1
    assert count("um word umum") == 1
    assert count("um umwordum um word um") == 3
