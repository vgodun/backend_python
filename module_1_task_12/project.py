contacts = {}
def add_contact():
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")

    contacts[name] = {
        "name": name,
        "email": email,
        "phone": phone,
    }

def search_contact():
    name = input("Name: ")
    for contact in contacts.values():
        if contact["name"] == name:
            print(contact)

def view_contacts():
    if not contacts:
        print("No contacts registered.")
    for item,key in contacts.items():
        print(f"{item}: {key}")

def update_contact():
    name = input("Name: ")
    if name in contacts:
        contacts[name]["phone"] = input("Phone: ")
        contacts[name]["email"] = input("Email: ")
def menu():
    while True:
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Exit")
        choice = input("You are select:  ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            break

        else:
            print("Not a valid choice.")

menu()



