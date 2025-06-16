from datetime import datetime
import os

def log_datetime(filename="log.txt"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists = os.path.exists(filename)

    with open(filename, "a") as file:
        file.write(now + "\n")

    if not file_exists:
        print(f"{filename} created.")
    print(f"Appended: {now}")

    print("\nFile content:")
    with open(filename, "r") as file:
        print(file.read().strip())

if __name__ == "__main__":
    log_datetime()
