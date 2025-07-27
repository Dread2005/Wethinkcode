
camel_case_input = input('Enter here: ')
snake = []
snake_ = []
indx = None
indxlst = []
caps = []
for n in camel_case_input:
    snake.append(n)
    if n.isupper():
        caps.append(n)
print(snake)

# while len(indxlst) != len(caps):
for item in snake:
    if item.isupper():
        snake.insert(int(snake.index(item)), '_')

print(snake)
# for n in snake:
#     if n.isupper():
#         indx = snake.index(n)
#         break
#     snake.insert(indx, '_')
#     continue

# snake_ = ' '.join(snake)
# print(snake_)