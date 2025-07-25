def main():
    time = input('What time is it?\nDo not leave any spaces when typing:  ').lower()
    time_lst = convert(time)
    #print((time_lst[0]))

    if type(time_lst[0]) == type(1) and type(time_lst[1]) == type(1):
        if time_lst[0] <= 12:
            print('Breakfast')
        elif time_lst[0] > 12 and time_lst[0] < 18:
            print('Lunch')
        else:
            print("Dinner")

    else:
        if time_lst[0] == 'am' and time_lst[1] <= 12:
            print('Breakfast')
        elif time_lst[0] == 'pm' and time_lst[1] >= 1 and time_lst[1] < 6:
            print("Lunch")
        elif time_lst[0] == 'pm' and time_lst[1] >= 6:
            print('Dinner')


def convert(time):
    if ":" in time:
        time_split = time.split(":")
        time_lst = [int(time_split[0]), int(time_split[1])]
    else:
        if len(time) == 4:
            time_split = [time[2:], int(time[:-2])]
        else:
            time_split = [time[1:], int(time[:-2])]
        time_lst = time_split
    print(time_lst)
    return time_lst

if __name__ == '__main__':
    main()