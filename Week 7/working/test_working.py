import pytest
from working import convert


def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("9:15 PM to 6:30 AM") == "21:15 to 06:30"

def test_convert_value():
    with pytest.raises(ValueError):
        convert("9AM - 5PM")

    with pytest.raises(ValueError):
        convert("22:00 to 8")

    with pytest.raises(ValueError):
        convert("29:00 to 27:00")

    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")