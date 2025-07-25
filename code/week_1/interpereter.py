maths = input('Expression:  ')
maths_lst = maths.split()
for n in maths_lst:
    if n == "+":
        print(float(maths_lst[0]) + float(maths_lst[-1]))
    elif n == "-":
        print(float(maths_lst[0]) - float(maths_lst[-1]))
    elif n == "/":
        print(float(maths_lst[0]) / float(maths_lst[-1]))
    elif n == "*":
        print(float(maths_lst[0]) * float(maths_lst[-1]))