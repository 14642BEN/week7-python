# Base class representing a Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Battery Life: {self.battery_life} hours")

    def charge(self):
        print("German machine charging...")

# Subclass inheriting from Smartphone, adding a specific feature
class Smartwatch(Smartphone):
    def __init__(self, brand, model, battery_life, watch_face):
        super().__init__(brand, model, battery_life)
        self.watch_face = watch_face  # example attribute specific to a smartwatch

    def display_info(self):
        super().display_info()
        print(f"Watch Face: {self.watch_face}")

    def charge(self):
        print("Charging the smartwatch with a special charging dock...")

# Creating objects
phone = Smartphone("Apple", "iPhone 15", 20)
watch = Smartwatch("Samsung", "Galaxy Watch 4", 48, "Digital")

# Displaying their information
phone.display_info()
watch.display_info()

# Charging
phone.charge()
watch.charge()
