def double(x):
    return x * 2

def square(x):
    return x **2

def add_five(x):
    return x + 5

def negate(x):
    return -x

def compose(*functions):
    def composed(x):
        for f in reversed(functions):
            x = f(x)
        return x
    return composed

def main():
    funcs = {
        "1": double,
        "2": square,
        "3": add_five,
        "4": negate
    }

    print("1: double  2: square  3: add_five  4: negate")
    selected = input("Enter the function numbers separated by commas (for example: 1,3): ").split(",")
    value = float(input("Enter number: "))

    chosen_funcs = [funcs[num.strip()] for num in selected if num.strip() in funcs]
    result = compose(*chosen_funcs)(value)

    print("Result:", result)

if __name__ == "__main__":
    main()
