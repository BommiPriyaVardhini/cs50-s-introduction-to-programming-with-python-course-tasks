import pytest
from twttr import shorten

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("CS50") == "CS50"
    assert shorten("AEIOU") == ""
    assert shorten("aeiou") == ""
    assert shorten("Hello, World!") == "Hll, Wrld!"
    assert shorten("") == ""
    assert shorten("Python") == "Pythn"
    assert shorten("12345") == "12345"
    assert shorten("CS50 rocks!") == "CS50 rcks!"
    assert shorten("abcdefghijklmnopqrstuvwxyz") == "bcdfghjklmnpqrstvwxyz"
    assert shorten("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "BCDFGHJKLMNPQRSTVWXYZ"

def test_numbers_and_punctuation():
    assert shorten("12345") == "12345"
    assert shorten("CS50!") == "CS50!"
    assert shorten("What's up?") == "Wht's p?"
    assert shorten("Goodbye.") == "Gdby."

if __name__ == "__main__":
    pytest.main()
