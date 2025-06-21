def uppercase_decorator(f):
    def wrapper():
        return f().upper()
    return wrapper


@uppercase_decorator
def great():
    return 'Hello'


print(great())