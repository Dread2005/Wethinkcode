groc_lst = []
amount = None
lst__amount = []


def grocery():
    lst = input()
    groc_lst.append(lst)

while '$' not in groc_lst:
    grocery_lst = grocery()
    #print(grocery_lst)

for n in groc_lst:
    if n not in lst__amount:
        lst__amount.append(f'{groc_lst.count(n)} {n}')
    
#del lst__amount[-1] 

for n in lst__amount:
    print(n)   