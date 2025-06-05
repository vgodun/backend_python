def triangle_pattern(n):
    for i in range(1, n + 1):
        print(*range(1, i + 1))


def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1,n + 1):
            print(f"{i * j : 4}", end=' ')
        print()


def countdown(start):
    while start > 0:
        print(start)
        start = start - 1


def main():
    while True:
        print("1. Triangle Pattern")
        print("2. Multiplication Table")
        print("3. Countdown")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            n = int(input("Enter number of rows: "))
            triangle_pattern(n)
        elif choice == "2":
            n = int(input("Enter table size "))
            multiplication_table(n)
        elif choice == "3":
            n = int(input("Enter number of rows: "))
            countdown(n)
        elif choice == "4":
            break

if __name__ == "__main__":
    main()