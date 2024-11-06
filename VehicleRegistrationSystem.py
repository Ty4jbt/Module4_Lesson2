# Task 1
# Objective: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicles owner. then, create a few instances of Vehicle and demonstrate changing of the owner.

# Declare a class Vehicle
class Vehicle:

    # Define the constructor, pass in registration_number, type, and owner
    def __init__(self, registration_number, type, owner):
        self.registration_number = registration_number
        self.type = type
        self.owner = owner

    # Define a method update_owner, pass in new_owner
    def update_owner(self, new_owner):
        self.owner = new_owner

# Create instances of the Vehicle class
car1 = Vehicle("ABC123", "Sedan", "John Doe")
car2 = Vehicle("DEF456", "SUV", "Jane Doe")
car3 = Vehicle("GHI789", "Truck", "John Smith")

# Print the current owner of each car
for i, car in enumerate([car1, car2, car3]):
    print(f"The current owner of car{i + 1} is {car.owner}")

# Update the owner of each car
car1.update_owner("Jane Smith")
car2.update_owner("Robert Smith")
car3.update_owner("Mary Smith")

# Print the new owner of each car
for i, car in enumerate([car1, car2, car3]):
    print(f"The new owner of car{i + 1} is {car.owner}")

