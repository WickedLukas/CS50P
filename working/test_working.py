import pytest

from working import convert


# Check if 12 AM and 12 PM are correctly converted.
def test_convert_12_AM_PM():
    assert convert("12:00 AM to 1:00 AM") == "00:00 to 01:00"
    assert convert("12:25 AM to 1:45 AM") == "00:25 to 01:45"
    assert convert("12:00 PM to 1:00 PM") == "12:00 to 13:00"
    assert convert("12:25 PM to 1:45 PM") == "12:25 to 13:45"
    assert convert("12:35 AM to 12:35 PM") == "00:35 to 12:35"
    assert convert("12:35 PM to 12:35 AM") == "12:35 to 00:35"


# Check if AM and PM are correctly converted.
def test_convert_AM_PM():
    assert convert("1:00 AM to 5:00 AM") == "01:00 to 05:00"
    assert convert("1:25 AM to 5:45 AM") == "01:25 to 05:45"
    assert convert("6:00 AM to 2:00 AM") == "06:00 to 02:00"
    assert convert("6:25 AM to 2:45 AM") == "06:25 to 02:45"
    assert convert("1:00 PM to 5:00 PM") == "13:00 to 17:00"
    assert convert("1:25 PM to 5:45 PM") == "13:25 to 17:45"
    assert convert("6:00 PM to 2:00 PM") == "18:00 to 14:00"
    assert convert("6:25 PM to 2:45 PM") == "18:25 to 14:45"
    assert convert("11:00 PM to 9:00 AM") == "23:00 to 09:00"
    assert convert("11:25 PM to 9:45 AM") == "23:25 to 09:45"


# Check if range limits are correctly converted.
def test_convert_in_range():
    assert convert("10:59 PM to 11:01 AM") == "22:59 to 11:01"
    assert convert("1:59 PM to 2:01 AM") == "13:59 to 02:01"
    assert convert("11:01 AM to 10:59 PM") == "11:01 to 22:59"
    assert convert("2:01 AM to 1:59 PM") == "02:01 to 13:59"


# Check if cases with no minutes are correctly converted.
def test_convert_no_min():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:12 AM to 5 PM") == "09:12 to 17:00"
    assert convert("9 AM to 5:45 PM") == "09:00 to 17:45"


# Check if ValueError is raised when range limits are exceeded.
def test_convert_out_range():
    with pytest.raises(ValueError):
        convert("-1:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to -5:00 PM")
    with pytest.raises(ValueError):
        convert("9:-01 AM to 5:01 PM")
    with pytest.raises(ValueError):
        convert("9:01 AM to 5:-01 PM")

    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 13:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")

    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 AM")
    with pytest.raises(ValueError):
        convert("9:00 PM to 13:00 AM")
    with pytest.raises(ValueError):
        convert("9:00 PM to 5:60 AM")
    with pytest.raises(ValueError):
        convert("9:60 PM to 5:00 AM")


# Check if ValueError is raised when the format is unexpected.
def test_convert_bad_format():
    with pytest.raises(ValueError):
        convert("0:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 0:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00 AB")
    with pytest.raises(ValueError):
        convert("9:00 AB to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:000 PM")
    with pytest.raises(ValueError):
        convert("9:000 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("a:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:aa AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to a:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:aa PM")
    with pytest.raises(ValueError):
        convert("9:00 AM ab 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM,5:00 PM")
    with pytest.raises(ValueError):
        convert("900 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 500 PM")
    with pytest.raises(ValueError):
        convert("900 AM to 500 PM")
