class Circle:
    radius = 6

    def get_area (self, pi):
        area = pi * self.radius ** 2
        return area
import math

my_circle = Circle()
area_circle = my_circle.get_area(math.pi)
print(area_circle)

circle_modified = Circle()
circle_modified.radius = 10
area_circle = circle_modified.get_area(math.pi)
print("circle modified " + str(area_circle))