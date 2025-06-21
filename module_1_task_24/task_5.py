numbers = [2, 4, 6, 8, 10]

even_squares = {x**2 for x in numbers if x % 2 == 0}

print(sorted(even_squares))
