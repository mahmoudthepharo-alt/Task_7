import math
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

def print_area(shape_object):
    print("Area:", shape_object.area())

print("Choose a shape:")
print(" 1- Circle")
print(" 2- Square")

choice = int(input("Enter your choice: "))

if choice == 1:
    radius = float(input("Enter the radius of the circle: "))
    shape = Circle(radius)
    print_area(shape)

elif choice == 2:
    side = float(input("Enter the side length of the square: "))
    shape = Square(side)
    print_area(shape)

else:
    print("Invalid choice.")