from random import randint


def main():
   int_gen = generate_integer(get_level())

   answer = int_gen[0] + int_gen[1]

   coun = 0

   bl = True
   while bl:

       print(f'{int_gen[0]} + {int_gen[1]} = ...')
       guess = int(input('Enter the answer: '))

       if guess == answer:
           print('Correct!')
           bl = False
       elif guess != answer:
           coun += 1
           print('Incorrect!')

           if coun == 3:
               print(f'answer: {answer}')
               bl = False





def get_level():
    try:
        level = int(input('Enter Level:'))
        if level > 3 or level <= 0:
            raise ValueError('Level can only be 1, 2, 3')
        if level == '':
            raise ValueError('Level cant be empty')
        return level
    except ValueError:
        print('Invalid Level')
        return get_level()



def generate_integer(level):
    int_lst = []

    if level == 1:
        int_1 = randint(1, 10)
        int_2 = randint(1, 10)
        int_lst.append(int_1)
        int_lst.append(int_2)

    elif level == 2:
        int_1 = randint(1, 50)
        int_2 = randint(1, 50)
        int_lst.append(int_1)
        int_lst.append(int_2)

    elif level == 3:
        int_1 = randint(1, 100)
        int_2 = randint(1, 100)
        int_lst.append(int_1)
        int_lst.append(int_2)

    return int_lst


if __name__ == "__main__":
    main()