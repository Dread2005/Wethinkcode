bank_greeting = input('Enter greeting: ').lower()
bank_greet_lst = bank_greeting.split()
first_wrd = bank_greeting[0].split()
if bank_greet_lst[0] == 'hello':
    print('R0')
elif first_wrd[0] == 'h' and bank_greet_lst[0] != 'hello':
    print('R20')
else:
    print("R100")
