from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self,diameter, radius):
        self.diameter = diameter
        self.radius = radius
    
    def calculate_perimeter(self):
        return self.diameter * math.pi
    
    def calculate_area(self):
        return math.pi * self.radius**2
        
class Square(Shape):
    def __init__(self, base):
        self.base = base
    
    def calculate_perimeter(self):
        return self.base * 4
    
    def calculate_area(self):
        return self.base ** 2

class Rectangle(Shape):
    def __init__(self, base, width):
        self.base = base
        self.width = width
    
    def calculate_perimeter(self):
        return (self.base + self.width)*2
    
    def calculate_area(self):
        return self.base * self.width


#Circle
circle_one = Circle(4,7)
perimeter = circle_one.calculate_perimeter()
print(perimeter)

area = circle_one.calculate_area()
print("Area: " + str(area))

#Square
square_one = Square(5)
perimeter = square_one.calculate_perimeter()
print(perimeter)

area = square_one.calculate_area()
print("Area: " + str(area))

#Rectangle
rectangle_one = Rectangle(8,4)

perimeter = rectangle_one.calculate_perimeter()
print(perimeter)

area = rectangle_one.calculate_area()
print("Area: " + str(area))