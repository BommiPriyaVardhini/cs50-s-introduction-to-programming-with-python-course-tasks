import pytest
from plates import is_valid

def test_length():
    assert not is_valid("A")          # Too short
    assert is_valid("AB")             # Minimum length
    assert is_valid("ABC")            # Valid length
    assert is_valid("ABCD")           # Valid length
    assert is_valid("ABCDE")          # Valid length
    assert is_valid("ABCDEF")         # Maximum length
    assert not is_valid("ABCDEFG")    # Too long

def test_start_with_two_letters():
    assert not is_valid("1A")         # Starts with digit
    assert not is_valid("A1")         # First character is a letter, second is a digit
    assert not is_valid("A1234")      # Starts with one letter followed by numbers
    assert not is_valid("1ABCDE")     # Starts with digit followed by letters
    assert is_valid("AB")             # Starts with two letters
    assert is_valid("ABC")            # Starts with three letters

def test_no_middle_numbers():
    assert is_valid("AB123")          # Digits at the end
    assert not is_valid("AB12C3")     # Letters in the middle of digits
    assert not is_valid("AB1C23")     # Letters in the middle of digits
    assert is_valid("ABC123")         # Digits at the end
    assert not is_valid("ABC12D")     # Letters after digits

def test_no_punctuation():
    assert is_valid("ABC123")         # No punctuation
    assert not is_valid("AB.CD1")     # Contains period
    assert not is_valid("AB CD1")     # Contains space
    assert not is_valid("AB,CD1")     # Contains comma
    assert not is_valid("AB;CD1")     # Contains semicolon

def test_no_leading_zero():
    assert not is_valid("AB0123")     # Leading zero in digits
    assert is_valid("AB123")          # Valid digits without leading zero
    assert is_valid("AB1")            # Single digit without leading zero

if __name__ == "__main__":
    pytest.main()
