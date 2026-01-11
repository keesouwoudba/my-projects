import pytest
from cookies import Jar


def test_init_default():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_init_invalid():
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar(3.5)
    with pytest.raises(ValueError):
        Jar("112")
        
def test_init_normal():
    jar = Jar(14)
    assert jar.capacity == 14
    
    
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "c"
    jar.deposit(2)
    assert str(jar) == "ccc"


def test_deposit_invalid():
    jar = Jar(5)
    with pytest.raises(ValueError):
        jar.deposit(6)
    jar.deposit(2)
    assert jar.size == 2
    

def test_withdraw():
    jar = Jar(10)
    jar.deposit(4)
    with pytest.raises(ValueError):
        jar.withdraw(5)
    jar.withdraw(3)
    assert jar.size == 1