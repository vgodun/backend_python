class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = float(salary)

    @classmethod
    def from_string(cls, data_str):
        name, salary = data_str.split(",")
        return cls(name.strip(), float(salary.strip()))

    @staticmethod
    def is_high_salary(salary):
        return salary > 100000

emp = Employee.from_string("Alice, 120000")

print(f"Employee name: {emp.name}, Salary: {emp.salary}")
print(f"Is the salary high? {Employee.is_high_salary(emp.salary)}")
