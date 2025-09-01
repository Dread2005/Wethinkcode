def main():
    tweet = input('Input: ').lower()
    print(vowl_checker(twtr(tweet)))

def twtr(tweet):
    update_tweet = None

    splt_tweet = list(tweet)
    return splt_tweet

def vowl_checker(twtr_func):
    vowls = ['a','e','i','o','u']
    try:
        for i in twtr_func:
            if i in vowls:
                twtr_func.remove(i)
                raise NameError
    except NameError:
        vowl_checker(twtr_func)

    update_tweet = ''.join(twtr_func)
    return update_tweet

if __name__ == '__main__':
    main()