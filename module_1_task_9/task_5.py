num1 = float(input('Enter a number: '))
num2 = float(input('Enter another number: '))

print('Enter first value: ',num1)

print('Enter second value: ',num2)

print(f'Before Swap: First Value = ${num1}, Second Value = ${num2}')

num1,num2 = num2,num1

print(f'After Swap: First Value = ${num1}, Second Value = ${num2}')