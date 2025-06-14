def make_adder(add_value):
    def add(x):
        print(x)
        return x+add_value
    return add

inc = make_adder(1)

print(inc(5))