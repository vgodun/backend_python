def main():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    color = input("Enter your favorite color: ")

    info = f"Name: {name}\nAge: {age}\nFavorite Color: {color}"

    with open("user_info.txt", "w") as file:
        file.write(info)

    print("Infromation add user_info.txt")

if __name__ == "__main__":
    main()
