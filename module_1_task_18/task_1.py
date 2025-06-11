class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year


get_car=Car(make = "Toyota", model = "Camry", year = 2025)

print(f"Make: {get_car.make} Model: {get_car.model} and Year: {get_car.year}" )