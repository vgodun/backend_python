def min_max_avg(numbers):
    if not numbers:
        return None, None, None

    if len(numbers) == 1:
        num= numbers[0]
        return num, num, None

    min_num = min(numbers)
    max_num = max(numbers)
    avg=sum(numbers) / len(numbers)

    return f"Min:{min_num}, Max:{max_num}, Avg:{avg}"

print(min_max_avg([1, 2, 3, 4, 5]))