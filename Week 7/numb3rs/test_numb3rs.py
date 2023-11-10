from numb3rs import validate

def test_validate_single_digit():
    assert validate("1.2.3.4") == True

def test_validate_double_digit():
    assert validate("10.10.10.10") == True

def test_validate():
    assert validate("192.168.178.10") == True
    assert validate("192.168.178.100") == True
    assert validate("192.168.178.567") == False
    assert validate("cat") == False
