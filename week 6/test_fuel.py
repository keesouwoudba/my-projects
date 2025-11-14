from fuel import gauge
from fuel import get_percent
import pytest


#check for /
def test_getpercent_ValueError():
    with pytest.raises(ValueError):
        get_percent("0/22/25")
        #for x>y
    with pytest.raises(ValueError):
        get_percent("15/10")
#checkk for 0
def test_get_percent_ZeroDivivsionError():
    with pytest.raises(ZeroDivisionError):
        get_percent("12/0")

def test_positivity_get_percent():
    with pytest.raises(ValueError):
        get_percent("-2/2")

    with pytest.raises(ValueError):
        get_percent("cat/dog")


def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(100) == "F"
    assert gauge(1) == "E"





