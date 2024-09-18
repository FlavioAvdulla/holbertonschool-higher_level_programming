class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def start_engine(self):
        return f"The engine of {self.model} made in {self.year} is running."

my_car = Car("Toyota", "Auris", 2023)
print(my_car.start_engine())