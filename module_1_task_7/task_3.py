a = True
b = False
c = True

# becouse both a and b need be a true
print(a and b)

#becouse at least one value True
print(a or b)

#becouse b it's true
print(not b)

#becouse a and c ture, and b false,why true?becouse  at least one value True
print((a and c) or b)

#becouse b or c becouse  at least one value True,and a true (b or c)  also true
print(a and (b or c))