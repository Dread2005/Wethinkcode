def main():
    name = input('Enter name: ')
    print(hello(name))

def hello(to = 'Hello world'):
    return f'hello my {to}'

if __name__ == '__main__':
    main()