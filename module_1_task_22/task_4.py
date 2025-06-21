import csv

def write_students_to_csv(filename):
    students = [
        ["Name", "Age", "Grade"],
        ["Alice", 25, "A"],
        ["Bob", 22, "B"],
        ["Charlie", 24, "A"]
    ]

    total_age = sum(int(row[1]) for row in students[1:])
    average_age = total_age / len(students[1:])

    students.append(["Average Age", f"{average_age:.2f}", ""])

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(students)

def read_and_display_csv(filename):
    print("File content:")
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == "Name":
                continue
            elif row[0] == "Average Age":
                print(f"\nAverage Age: {row[1]}")
            else:
                print(f"Name: {row[0]}, Age: {row[1]}, Grade: {row[2]}")

def main():
    filename = "students.csv"
    write_students_to_csv(filename)
    read_and_display_csv(filename)

if __name__ == "__main__":
    main()
