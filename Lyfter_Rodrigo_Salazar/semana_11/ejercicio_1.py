import math

class Circle:
    def __init__(self,radius):
        self.radius =  radius

    def get_area (self, pi):
        area = pi * self.radius ** 2
        return area


my_circle = Circle(6)
area_circle = my_circle.get_area(math.pi)
print(area_circle)

circle_modified = Circle(10)
area_circle = circle_modified.get_area(math.pi)
print("circle modified " + str(area_circle))