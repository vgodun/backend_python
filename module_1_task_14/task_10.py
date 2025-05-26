numbers = [1,2,3,4,5]

double = map(lambda num: num*2, numbers)

filtered = filter(lambda x: x < 10, double)

print(list(filtered))