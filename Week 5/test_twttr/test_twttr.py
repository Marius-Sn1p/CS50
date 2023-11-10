from twttr import shorten

def test_shorten_vowels():
    assert shorten("aeiou")== ""
    assert shorten("tom") == "tm"

def test_shorten_no_vowels():
    assert shorten("dry") == "dry"
    assert shorten("spy") == "spy"

def test_shorten_no_input():
    assert shorten("")==""

def test_shorten_nums():
    assert shorten("b1k3") == "b1k3"

def test_shorten_upper_case():
    assert shorten("TonGuE") == "TnG"

def test_shorten_spec_chat():
    assert shorten("h3llo+,") == "h3ll+,"