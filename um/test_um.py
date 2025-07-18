import um

def test_single_um():
    assert um.count("um") == 1
    assert um.count("Um") == 1
    assert um.count("UM") == 1

def test_multiple_ums():
    assert um.count("um, um, um.") == 3
    assert um.count("Um... um... UM!") == 3

def test_um_as_substring():
    assert um.count("yummy") == 0
    assert um.count("umbrella") == 0
    assert um.count("gum") == 0

def test_um_with_punctuation():
    assert um.count("hello, um, world") == 1
    assert um.count("um?") == 1
    assert um.count("um!") == 1

def test_no_um():
    assert um.count("hello world") == 0
    assert um.count("") == 0

if __name__ == "__main__":
    test_single_um()
    test_multiple_ums()
    test_um_as_substring()
    test_um_with_punctuation()
    test_no_um()
    print("All tests passed.")
