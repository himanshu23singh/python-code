class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Polymorphic behavior
animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.speak()


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload the '+' operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 4)

print(v1 + v2)  # Output: (3, 7)