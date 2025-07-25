def main():
    time = input('What time is it? ').lower()
    time_lst = convert(time)
    #print(type(time_lst[0]))

    if type(time_lst[0]) == type(1):
        if time_lst[0] <= 12:
            print('Breakfast')
        elif time_lst[0] > 12 and time_lst[0] < 18:
            print('Lunch')
        else:
            print("Dinner")

    else:
        if 'am' in time_lst and time_lst[0] < 12:
            print('Breakfast')
        elif 'pm' in time_lst and time_lst[0] >= 12 and time_lst[0] < 18:
            print("Lunch")
        else:
            print('Dinner')


def convert(time):
    if ":" in time:
        time_split = time.split(":")
        time_lst = [int(time_split[0]), int(time_split[1])]
    else:
        time_split = [int(time[:-2]), time[2:]]
        time_lst = time_split
    return time_lst

if __name__ == '__main__':
    main()