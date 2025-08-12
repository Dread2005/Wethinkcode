import pyfiglet
from pyfiglet import Figlet


def func():
    try:
        font_change = input('Enter Font(not compulsory): ')
        value = input('Enter word or sentence: ')

        font_change_lst = font_change.split(' ')

        if font_change == '':
            f = Figlet(font='slant')
            print(f.renderText(value))
        if font_change != '':
            if font_change_lst[0] == '-f' or font_change_lst[0] == '--font':
                font_init = str(font_change_lst[0]).lower()
                font_ = str(font_change_lst[1]).lower()
                f = pyfiglet.figlet_format(text=value, font=font_)
                print(f"Output:\n\n{f}")
            else:
                raise ValueError()
    except ValueError:
        print('Invalid usage')
        return func()
func()