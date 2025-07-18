from seasons import minutes_lived
def main():
    test_1()
    test_2()
def test_1():
    assert_minutes_lived(2003, 5, 17)=="Ten million, fifty-eight thousand, four hundred minutes"
    assert_minutes_lived(2000, 2, 1)=="Eleven million, seven hundred eighty-seven thousand, eight hundred forty minutes"
def test_2():
    assert_minutes_lived(23, 1, 2000)== "Invalid Date"
if __name__ == "__main__":
    main()
