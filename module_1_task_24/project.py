raw_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in raw_data]
print("Squares of all numbers:", squares)

even_squares = [x**2 for x in raw_data if x % 2 == 0]
print("Squares of even numbers:", even_squares)

squares_dict = {x: x**2 for x in raw_data}
print("Dictionary (number → square):", squares_dict)

unique_large_squares = {x**2 for x in raw_data if x > 5}
print("Unique squares of numbers > 5:", unique_large_squares)

nested_data = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
flattened = [item for sublist in nested_data for item in sublist]
print("Flattened list:", flattened)

grouped = {
    "even": [x for x in raw_data if x % 2 == 0],
    "odd": [x for x in raw_data if x % 2 != 0]
}
print("Grouped numbers (even/odd):", grouped)

meta_info = {
    x: {"even": x % 2 == 0, "square": x**2}
    for x in raw_data
}
print("Metadata for each number:", meta_info)
