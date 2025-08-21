from calc import square
import pytest

def main():
    test_poss()
    test_neg()
    test_0()
    type_str()

def test_poss():
    assert square(2) == 4
    assert square(3) == 9

def test_neg():
    assert square(-3) == 9
    

def test_0():
    assert square(-2) == 4
    assert square(0) == 0

#Cathing exceptions with pytest:
def type_str():
    with pytest.raises(TypeError):
        square('cat')

if __name__ == '__main__':
    main()