class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50
        self.happiness = 50

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 10
            if self.hunger < 0:
                self.hunger = 0
            print(f"{self.name} has been fed. Hunger decreased.")
        else:
            print(f"{self.name} is not hungry.")

    def play(self):
        if self.happiness < 100:
            self.happiness += 10
            if self.happiness > 100:
                self.happiness = 100
            print(f"{self.name} played and is happier now.")
        else:
            print(f"{self.name} is already very happy!")

    def status(self):
        print(f"Status of {self.name}:")
        print(f"  Species: {self.species}")
        print(f"  Hunger: {self.hunger}/100")
        print(f"  Happiness: {self.happiness}/100")


def main():
    print("Welcome to the Pet Simulator!")
    name = input("Enter your pet's name: ")
    species = input("Enter the species (e.g., dog, cat): ")

    pet = Pet(name, species)

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Check status")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.status()
        elif choice == "4":
            print(f"Goodbye! {pet.name} will miss you")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
