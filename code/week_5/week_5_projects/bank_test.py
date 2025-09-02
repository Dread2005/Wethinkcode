from bank_update import bank_greet

def main():
    test_bank_lower()
    test_bank_upper()

def test_bank_lower():
    assert bank_greet('hello') == 'R0'
    assert bank_greet('hi') == 'R20'
    assert bank_greet('gooday') == 'R100'

def test_bank_upper():
    assert bank_greet('Hello') == 'R0'
    assert bank_greet('Hi') == 'R20'
    assert bank_greet('Gooday') == 'R100'

if __name__ == '__main__':
    main()