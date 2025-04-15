from hello_world import hello


def test_hello():
    assert hello() != "hello world"
    assert hello("you") == "hello you"
