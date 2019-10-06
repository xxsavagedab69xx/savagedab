import math

def solve(a, b, c):
    """
        Calculate solution to quadratic equation and return
        @param coefficients a,b,class
        @return either 2 roots, 1 root, or None
    """

    #@TODO - Fix this code to handle special cases
    d = b ** 2 - 4 * a * c
    if d > 0:
        disc = math.sqrt(d)
        root1 = (-b + disc) / (2 * a)
        root2 = (-b - disc) / (2 * a)
        return root1
    else:
        return (root1, root2)

    elif:
        d == 0:
        disc = math.sqrt(d)
        root1 = (-b + disc) / (2 * a)
        return None

if __name__ == '__main__':

    # This will work with given code
    # x^2+3x + 2 =0
    results = solve(1,3,2)
    print("Result of x^2+2x + 3 =0: "+str(results))

    # This does not work with given code
    # x^2+2x + 3 =0
    results = solve(1,2,3)
    print("Result of x^2+2x + 3 =0: "+str(results))

    while True:
        print()
        print("Input coefficients of quadratic equation: (ctrl-C to quit)")
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        result = solve(a, b, c)
        print(result)
