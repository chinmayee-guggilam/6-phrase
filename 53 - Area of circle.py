'''Define a class named Circle which can be constructed by a radius. The 
Circle class has a method which can compute the area.'''
#Code
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return math.pi * (self.radius ** 2)

# Example usage
circle = Circle(5)
area = circle.compute_area()
print("Area of the circle:", area)

#Output
'''
Area of the circle: 78.53981633974483
'''
