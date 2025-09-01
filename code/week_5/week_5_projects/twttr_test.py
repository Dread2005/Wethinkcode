from twttr_Update import vowl_checker
from twttr_Update import twtr
def main():
    test_twtr()

def test_twtr():
    assert vowl_checker(twtr('dread ford')) == 'drd frd'
    
if __name__ == '__main__':
    main()