from seasons import get_minutes

def test_get_minutes():
    assert get_minutes(365) == "Five hundred twenty-five thousand, six hundred minutes"
    assert get_minutes(730) == "One million, fifty-one thousand, two hundred minutes"