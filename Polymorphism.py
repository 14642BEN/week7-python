# Base class representing a generic Vehicle
class Vehicle:
    def move(self):
        print("This vehicle moves...")

# Car class that defines move() differently
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Plane class that defines move() differently
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Boat class that defines move() differently
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Creating instances of different vehicles
vehicles = [Car(), Plane(), Boat()]

# Demonstrating polymorphism (same method, different behavior)
for vehicle in vehicles:
    vehicle.move()
