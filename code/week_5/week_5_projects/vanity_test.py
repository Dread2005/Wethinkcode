from vanity_update import is_valid

def main():
    test_vanity()

def test_vanity():
    assert is_valid('Hello') == True
    assert is_valid('hello, world') == False

def test_0_vanity():
    assert is_valid('Hell10') == True
    assert is_valid('0hello') == False

if __name__ == '__main__':
    main()