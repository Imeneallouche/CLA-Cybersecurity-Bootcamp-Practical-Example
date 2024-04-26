class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Overloading example within a class
class Calculator():
    def add(self, a, b):
        return a + b 

    def add(self, a, b, c):
        return a + b + c

# Overriding example
rectangle = Rectangle(5, 4)
print("Rectangle area:", rectangle.area())           # This will print 20
print("Rectangle perimeter:", rectangle.perimeter())  # This will print 18

circle = Circle(3)
print("Circle area:", circle.area())                 # This will print 28.26 (approx.)
print("Circle perimeter:", circle.perimeter())       # This will print 18.84 (approx.)

# Overloading example within a class
cal = Calculator()
print("Calculator addition (2 params):", cal.add(2, 3))      # This will print 5
print("Calculator addition (3 params):", cal.add(2, 3, 4))   # This will print 9
