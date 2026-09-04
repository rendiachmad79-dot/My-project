from myproject.main import greet


def test_greet_default() -> None:
    assert greet("Budi") == "Hello, Budi."


def test_greet_excited() -> None:
    assert greet("Budi", excited=True) == "Hello, Budi!"
