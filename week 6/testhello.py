from helloworld import hello


def testhello():
    assert hello("david") == "hello, david"

def testdefault():
    assert hello() == "hello, world"