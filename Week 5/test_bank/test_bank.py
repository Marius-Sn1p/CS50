from bank import value

def test_value_punc():
    assert value("hello.") == 0
    assert value("!hello") == 100

def test_value():
    assert value("good day") == 100
    assert value("hi") == 20

def test_value_num():
    assert value("h3ll0") == 20

def test_value_uppercase():
    assert value("HELLO WORLD") == 0
    assert value("GOOD DAY") == 100