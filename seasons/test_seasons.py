from seasons import convert_to_minutes, convert_minutes_to_words

import pytest
from datetime import date, timedelta

def test_convert_to_minutes():
    '''
    Test seasons.convert_to_minutes() including rounding.
    '''
    assert convert_to_minutes(timedelta(minutes=0)) == 0
    assert convert_to_minutes(timedelta(minutes=15)) == 15
    assert convert_to_minutes(timedelta(minutes=315)) == 315
    assert convert_to_minutes(timedelta(seconds=0)) == 0
    assert convert_to_minutes(timedelta(seconds=60)) == 1
    assert convert_to_minutes(timedelta(seconds=300)) == 5
    assert convert_to_minutes(timedelta(seconds=315)) == 5
    assert convert_to_minutes(timedelta(seconds=345)) == 6
    assert convert_to_minutes(timedelta(hours=1)) == 60
    assert convert_to_minutes(timedelta(hours=5)) == 300
    assert convert_to_minutes(timedelta(hours=5, minutes=15)) == 315
    assert convert_to_minutes(timedelta(hours=5, minutes=15, seconds=15)) == 315
    assert convert_to_minutes(timedelta(hours=5, minutes=15, seconds=45)) == 316


def test_convert_minutes_to_words():
    '''
    Test seasons.convert_minutes_to_words().
    '''
    assert convert_minutes_to_words(315) == "Three hundred fifteen minutes"
    assert convert_minutes_to_words(-315) == "Minus three hundred fifteen minutes"
    assert convert_minutes_to_words(3456) == "Three thousand, four hundred fifty-six minutes"
    assert convert_minutes_to_words(-3456) == "Minus three thousand, four hundred fifty-six minutes"
    assert convert_minutes_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
