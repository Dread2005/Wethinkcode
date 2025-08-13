song = 'Adieu, adieu, to '
and_ = 'and'
name_lst = []

def song_names():
    name = input('Enter name: ').capitalize()
    name_lst.append(name)
    if name.lower() == '-d':
        del name_lst[-1]
        return None
    return song_names()

try:
    song_names()
    last_name = and_ + ' ' + str(name_lst[-1])
    if len(name_lst) == 1:
        raise TypeError()
    del name_lst[-1]
    full_song = song + ', '.join(name_lst) + ' ' + last_name
    print(full_song)

except TypeError:
    full_song = song + name_lst[0]
    print(full_song)


