def function():
    ans = None
    fraction = input('Fraction: ')
    frac_splt = fraction.split('/')
    try:
        for i in frac_splt:
            frac_splt[frac_splt.index(i)]  = int(i)
        #print(frac_splt)
        ans = int((frac_splt[0]/frac_splt[1])*100)
        if ans < 0:
            raise ValueError
    except(ValueError, TypeError, ZeroDivisionError):
        return function()


    if ans == 100:
        ans = 'Full'
    elif ans == 0:
        ans = 'Empty'

    if type(ans) is str:
        return ans
    elif type(ans) is int:
        ans = f'%{ans}'
        return ans

func = function()
print(func)

# try:
#     print(function())
# except(ValueError, TypeError, ZeroDivisionError):
#     print(function())