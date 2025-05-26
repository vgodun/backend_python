password = input("Enter password: ")

if len( password) < 8:
    print("Password is invalid. Reason: Less than 8 characters.")
elif ' ' in password:
    print("Password is invalid. Reason: Contains spaces.")
elif "Python" not in password:
    print("Password is invalid. Reason: Does not contain 'Python'")
else:
    print("Password is valid.")
