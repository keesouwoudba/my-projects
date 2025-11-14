from week6 import square
import pytest


def test_positives_square():
        assert square(2) == 4
        assert square(3) == 9

def test_negatives_square():
        assert square(-2) == 4

def test_0_square():
        assert square(0) == 0

def test_str():
        with pytest.raises(TypeError):
                square("cat")
    
#hello