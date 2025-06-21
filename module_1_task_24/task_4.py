nested_list = [[1, 2, 3], [4, 5], [6, 7]]

flat_gen = (item for sublist in nested_list for item in sublist)

flat_list = list(flat_gen)

print(flat_list)
