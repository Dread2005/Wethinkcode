def main():
    print(twtr())

def twtr():
    vowls = ['a','e','i', 'o','u']
    update_tweet = None
    tweet = input('Input: ').lower()

    splt_tweet = list(tweet)
    #print(splt_tweet)

    for i in splt_tweet:
        if i in vowls:
            splt_tweet.remove(i)

    update_tweet = ''.join(splt_tweet)
    return update_tweet

if __name__ == '__main__':
    main()