from task_4 import ElectricCar

class ElectricCarNew(ElectricCar):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year, battery_size)


car = ElectricCarNew("Tesla", "Model X", 2023, 120)

print(car.make, car.model, car.year, car.battery_size)