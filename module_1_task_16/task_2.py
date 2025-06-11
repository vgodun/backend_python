numbers = [10, 20, 30, 40, 50, 11, 17, 22]

sum = 0
count = 0

for num in numbers:
    if num % 2 == 0:
        sum += num
        count += 1


print("Sum of even numbers: ",sum)
print("Number of even numbers: ",count)
