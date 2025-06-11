class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False


person1 = Person("Alice", 18)
person2 = Person("Alice", 18)

print(f"Are they equal? {person1 == person2}")