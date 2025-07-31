def function():
    ans = None
    fraction = input('Fraction: ')
    frac_splt = fraction.split('/')

    for i in frac_splt:
        frac_splt[frac_splt.index(i)]  = int(i)
        #print(frac_splt)
    ans = (frac_splt[0]/frac_splt[1])*100

    if ans == 100:
        ans = 'Full'
    elif ans == 0:
        ans = 'False'

    if type(ans) is str:
        return ans
    elif type(ans) is int or type(ans) is float:
        ans = f'%{ans}'
        return ans
        

try:
    print(function())
except(ValueError, TypeError, ZeroDivisionError):
    print(function())