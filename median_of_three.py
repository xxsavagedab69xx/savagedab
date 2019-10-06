# FIXME 3: define the function here.

def median(a, b, c):
    if (a > b and a < c) or (a < b and a > c):
        mediann = a

    elif (b > a and b < c) or (b < a and b > c):
        mediann = b

    else:
        mediann = c

    return mediann

if __name__ == "__main__":
    # FIXME 1: Print the statement where you say what the program is going to do

    print('This Program finds the median value of three numbers entered by the user.')
        
    # FIXME 2: Propmt the user to input 3 numbers

    a = int(input('Input first number:\n'))
    b = int(input('Input second number:\n'))
    c = int(input('Input third number:\n'))

    # FIXME 3: Call the median function and print the result
    print('The median is', median(a, b, c))