def double(func):
    def wrap():
        return func() * 2
    return wrap

def add_five(func):
    def wrap():
        return func() +5
    return wrap

@add_five
@double
def get():
    return 10

print(get())