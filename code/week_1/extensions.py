ext_dict = {'gif': 'Image', 'jpg': 'image', 'jpeg': 'image', 'png':'image', 'pdf':'text file', 'txt':'text file', 'zip':'zip file'}
file_ = input('File name: ')
split_file = file_.split(".")
file_type = ' '
print(split_file)
if split_file[-1] in ext_dict:
    file_type = f'{ext_dict[split_file[-1]]}/{split_file[-1]}'
print(file_type)