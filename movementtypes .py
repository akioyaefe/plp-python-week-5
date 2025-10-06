# ====================================
# Activity 2: Polymorphism Challenge 🎭
# ====================================

# Parent class
class Vehicle:
    def move(self):
        print("Vehicle is moving in a general way...")

# Child class 1
class Car(Vehicle):
    def move(self):
        print("🚗 The car is driving on the road.")

# Child class 2
class Plane(Vehicle):
    def move(self):
        print("✈️ The plane is flying in the sky.")

# Child class 3
class Boat(Vehicle):
    def move(self):
        print("🚤 The boat is sailing on the water.")

# Child class 4
class Bicycle(Vehicle):
    def move(self):
        print("🚴 The bicycle is pedaling along the path.")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    v.move()  # Each one behaves differently, even though the method name is the same
