coke_price = 50
due = 50
only_elig = [25, 10, 5]
def coin_input():
    global due
    while due != 0:
        coin = int(input('inser coin:'))
        if coin in only_elig:
            amount_due = coke_price - coin
            due -= coin
            if due != 0:
                print(f'amount due: {due}')
        else:
            print('Not eligable')
    return 'COKE'
    
coke_mach = coin_input()
print(coke_mach)