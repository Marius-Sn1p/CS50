from plates import is_valid

def test_is_valid_begin_letter():
    assert is_valid("CS") == True
    assert is_valid("C5") == False
    assert is_valid("50") == False

def test_is_valid_length():
    assert is_valid("TESTINCS50") == False
    assert is_valid("CS") == True
    assert is_valid("MECS50") == True

def test_is_valid_num():
    assert is_valid("AAA111") == True
    assert is_valid("BB22BB") == False
    assert is_valid("CCC000") == False

def test_is_valid_punc():
    assert is_valid("!CS50") == False
    assert is_valid("CS50!") == False
    assert is_valid("CS!50") == False