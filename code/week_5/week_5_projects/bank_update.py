def main():
    bank_greeting = input('Enter greeting: ')
    print(bank_greet(bank_greeting))

def bank_greet(bank_greating):
    bank_greet_lst = bank_greating.lower().split()
    first_wrd = bank_greating[0].lower().split()
    print(first_wrd)
    if bank_greet_lst[0] == 'hello':
        return 'R0'
    elif first_wrd[0] == 'h' and bank_greet_lst[0] != 'hello':
        return 'R20'
    else:
        return "R100"

if __name__ == '__main__':
    main()
