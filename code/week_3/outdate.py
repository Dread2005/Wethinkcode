word_lst = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

date_0_absent = list(range(1, 10))
date_num_lst = ['01','02','03','04','05','06','07','08','09', '10', '11', '12']
print(date_num_lst)
print(date_0_absent)

def date_func ():
    word = input('YYYY-MM-DD: ')
    date = None
    try:
        input_lst_num = word.split('/')
        for n in input_lst_num:
            print(n)
            if n in date_0_absent
        if len(input_lst_num) <= 1:
            raise TypeError
            
    except TypeError:
        input_lst_wrd = word.split()
        for n in input_lst_wrd:
            print(n)

date_func()
        