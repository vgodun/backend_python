square_number = float(input("Enter a number: "))


def square(x):
    return x ** 2


square_lambda = lambda x: x ** 2

print(square_lambda(square_number))
