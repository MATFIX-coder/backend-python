from abc import *

class Vehicle(ABC):
    def __init__(self, name, year):
        self.name = name
        self.year = year

    @abstractmethod
    def describe(self):
        pass

class Car(Vehicle):
    def describe(self):
        return f"Car: {self.name}, {self.year}"

class Bus(Vehicle):
    def describe(self):
        return f"Bus: {self.name}, {self.year}"

class Aeroplane(Vehicle):
    def describe(self):
        return f"Aeroplane: {self.name}, {self.year}"

def print_info(vehicle):
    print(vehicle.describe())

car = Car("Car", 2020)
bus = Bus("Bus", 2020)
aeroplane = Aeroplane("Aeroplane", 2020)

print_info(car)
print_info(bus)
print_info(aeroplane)
