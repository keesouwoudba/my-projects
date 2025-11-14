from twttr import shorten


def test_string():
    assert shorten("hello, world") == "hll, wrld"

def test_number():
    assert shorten("123bye") == "123b"