numbers = [3, 7, 1, 9, 4]

for i,num in enumerate(numbers):
    num *= 3
    if num > 15:
        numbers[i] = "Too large"


print(numbers)