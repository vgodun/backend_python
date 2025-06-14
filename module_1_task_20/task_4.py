def multiply_decorator(fac):
    return lambda f: lambda: f() * fac

@multiply_decorator(2)
def get_price():
    return 50

print(get_price())
