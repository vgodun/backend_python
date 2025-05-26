from functools import reduce

numbers = [1,2,3,4,5,6,7,8,9]

acc = []

reduce(lambda total,x: acc.append(total + x) or total + x, numbers,0)

print(acc)