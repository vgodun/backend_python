words = ["apple", "banana", "cherry", "apricot", "blueberry"]

target = "a"

filtered_words = list(filter(lambda word: word.startswith(target), words))
print(filtered_words)