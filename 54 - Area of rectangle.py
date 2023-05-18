'''Define a class named Rectangle which can be constructed by a length and 
width. The Rectangle class has a method which can compute the area.'''
#Code
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

# Example usage
rectangle = Rectangle(4, 6)
area = rectangle.compute_area()
print("Area of the rectangle:", area)

#Output
'''
Area of the rectangle: 24
'''
