menu = {"Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00}

total = 0

def order():
    try:
        global menu
        global total
        order_price = []
        wrd_lst = []
        comp = None
        pay = input('enter order: ')

        while pay != '$':
            if pay.isdigit():
                raise ValueError
            
            wrd_lst = pay.split()
            #print(pay)

            for i in wrd_lst:
                order_price.append(i.capitalize())

            comp = ' '.join(order_price)
            #print(comp)
            if comp not in menu:
                comp = None
                #print(f'{comp} clear' )
                raise ValueError
            total += menu[comp]
            print('Order accepted')
                
        return comp
            
    except(ValueError):
        return order()
            

    
ord_ = order()
print(f'Your total is {total}')
