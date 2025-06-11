class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class ElectricCar(Vehicle):
    def __init__(self, make, model, year,battery_size):
        super().__init__(make,model,year)
        self.battery_size = battery_size


get_car = ElectricCar("Audi", "e-tron", 2019, 100)

print(f"{get_car.make}, {get_car.model}, {get_car.year}, {get_car.battery_size}")
