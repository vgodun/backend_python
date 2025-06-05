name = input("Enter your name: ")
title = input("Enter your title: ")

def format_name(name, title="Mr./Ms."):
    first_name = name.split()[0]
    if title == "man":
        return f"Mr., Name: {first_name}"
    else:
        return f"Ms., Name: {first_name}"

print(format_name(name, title))

