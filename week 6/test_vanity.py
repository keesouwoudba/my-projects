from vanity import is_valid

def test_hello():
    assert is_valid("HELLO") == True

def test_hellocommaworld():
    assert is_valid("HELLO, WORLD") == False
def test_goodgye():
    assert is_valid("GOODBYE") == False
def test_CS50():
    assert is_valid("CS50") == True
def test_CS05():
    assert is_valid("CS05") == False
def test_50():
    assert is_valid("50") == False
def test_CS50P():
    assert is_valid("CS50P") == False
