from string_test_file import hello

def main():
    test_str()

def test_str():
    assert hello('Daavid') == 'hello my Daavid'

if __name__ == '__main__':
    main()