import pytest
from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello there") == 0

def test_h():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("hola") == 20
    assert value("Hi there") == 20

def test_other():
    assert value("good morning") == 100
    assert value("what's up") == 100
    assert value("Greetings") == 100
    assert value("Salutations") == 100

if __name__ == "__main__":
    pytest.main()

