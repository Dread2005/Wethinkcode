def main():
    plate = input('Plate: ')

    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')

def is_valid(s):
    na = [',', ' ', '.']
    ints = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    plate_lst = list(s)
    print(plate_lst)
    print(len(plate_lst))
    for n in plate_lst[0:-3]:
        if n not in ints:
            continue
        else:
            invalid(s)
    if len(plate_lst) > 2 and len(plate_lst) <= 6:
        #print('first_step')
        if type(plate_lst[0]) is str and type(plate_lst[1]) is str:
            #print('second_step')
            if plate_lst[-1] in ints or plate_lst[-1] == '0' or ints not in plate_lst:
                if plate_lst[-2] != '0':
                    #print('third step')
                    return True
    else:
        return invalid(s)
        
def invalid(t):
    plate_lst = list(t)
    na = [',', ' ', '.']
    ints = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    if plate_lst[0] in ints:
        return False
    if '0' in plate_lst and '0' != plate_lst[-1]:
        return False
    if na in plate_lst:
            return False
    if plate_lst[0] or plate_lst[1] in ints:
        return False
    if len(plate_lst) > 6 or len(plate_lst) < 2:
        return False
    
if __name__ == '__main__':
    main()