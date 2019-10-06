# FIXME 3: use a loop to iterate 10 times and print the multiplication table one row at a time.
def multiplication(n):
    for i in range(1, 11):
        print(n, 'x', i, '=', (n*i))

if __name__ == "__main__":
    # FIXME 1: print instructions
    print('This program will create the multiplication table of a number\n')

    # FIXME 2: Prompt the user to input a number
    num = int(input('Please input a number:\n'))

    # FIXME call the multiplication function
    print('The multiplication table of', num, 'is:')
    multiplication(num)