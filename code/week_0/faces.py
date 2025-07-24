faces = input()
face_lst = [':)', ':(']
word_list = faces.split()
print(word_list)
for n in word_list:
    if n == face_lst[0]:
        word_list[word_list.index(n)] = "😊"
    elif n == face_lst[1]:
        word_list[word_list.index(n)] = "😕"
word_lst = " ".join(word_list)
print(word_lst)