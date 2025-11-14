from bank import greeting

def test_starting_with_hello():
    assert greeting("hello, jack") == 0
    assert greeting("hello, bob") == 0

def test_starting_with_h():
    assert greeting("hey, bro, hows life") == 20
    assert greeting("how's it going") == 20

def test_else():
    assert greeting("jack, what's up") == 100
    assert greeting("what's up bro") == 100
    assert greeting("eeeee, assalomu aleykum, bro") == 100
