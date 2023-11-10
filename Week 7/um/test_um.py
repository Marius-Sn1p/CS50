import pytest
from um import count

def test_count():
    assert count("Um, what a spectrum.") == 1
    assert count("um") == 1
    assert count("um, bye, Um..") == 2
    assert count("Um.") == 1
