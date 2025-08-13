from random import randint
value = randint(1, 100)
def game():
    try:
        answer = int(input('add your answer: '))
        if answer > value:
            print('Too big')
            raise ValueError()
        elif answer < value:
            print ('Too small')
            raise ValueError()
        elif answer == value:
            return 'You win'
    except ValueError:
        return game()
print(game())