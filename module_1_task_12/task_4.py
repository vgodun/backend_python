phone_book = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-123-4567"
}

for key,value in phone_book.items():
    if key == "Alice":
        print("Alice's phone number: ", value)



del phone_book["Bob"]

print(phone_book)
