class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

# Creating an object
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.display_info())