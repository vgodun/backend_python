x = 500
y = 500

z = x
u = y
print(z is x)
print(u is y)

p = 10
q = 10
p += 0
o = p
w = q
print(o is p)
print(o is q)
print(id(p))
print(id(q))
print('p+0', p)