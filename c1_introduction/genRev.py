import math

number = int(input("Please, enter an integer: "))

while True:
    try:
        math.sqrt(number)
    except ValueError:
        print("Invalid number")
        number = int(input("Enter valid number: "))
    else:
        print(math.sqrt(number))
        break


# Newton's Method for approximating square root.
def squareroot(n):
    """User Newton's Method to approximate square root of n"""
    root = n/2  # Initial guess will be n/2
    for k in range(20):
        root = (1/2) * (root + (n / root))

    return root

