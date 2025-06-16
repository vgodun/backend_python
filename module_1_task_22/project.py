import os

NOTES_DIR = "notes"

os.makedirs(NOTES_DIR, exist_ok=True)

def create_note():
    title = input("Enter note title: ").strip()
    content = input("Enter note content: ")

    filename = os.path.join(NOTES_DIR, f"{title}.txt")

    try:
        with open(filename, "w") as file:
            file.write(content)
        print(f"Note '{title}' saved.")
    except Exception as e:
        print(f"Error saving note: {e}")

def read_note():
    title = input("Enter note title to read: ").strip()
    filename = os.path.join(NOTES_DIR, f"{title}.txt")

    try:
        with open(filename, "r") as file:
            print("Note content:")
            print(file.read())
    except FileNotFoundError:
        print("Note not found.")
    except Exception as e:
        print(f"Error reading note: {e}")

def list_notes():
    notes = [f for f in os.listdir(NOTES_DIR) if f.endswith(".txt")]
    if notes:
        print("Available notes:")
        for note in notes:
            print("–", note[:-4])
    else:
        print("No notes found.")

def search_notes():
    keyword = input("Enter keyword to search: ").lower()
    found = False

    for filename in os.listdir(NOTES_DIR):
        if filename.endswith(".txt"):
            filepath = os.path.join(NOTES_DIR, filename)
            with open(filepath, "r") as file:
                content = file.read().lower()
                if keyword in content:
                    print(f"Found in '{filename[:-4]}'")
                    found = True

    if not found:
        print("No matches found.")

def main():
    while True:
        print("Notes Menu:")
        print("1. Create a note")
        print("2. Read a note")
        print("3. List all notes")
        print("4. Search notes")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            create_note()
        elif choice == "2":
            read_note()
        elif choice == "3":
            list_notes()
        elif choice == "4":
            search_notes()
        elif choice == "5":
            print("Exiting Notes App.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
