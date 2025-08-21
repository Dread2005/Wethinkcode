def main():
    x = input('Enter here: ')
    print(f'{x} squared = {square(x)}')

def square(x):
    return x * x
if __name__ == '__main__':
    main()