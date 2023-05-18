'''Define a class named Shape and its subclass Square. The Square class has an 
init function which takes a length as argument. Both classes have a area 
function which can print the area of the shape where Shape's area is 0 by 
default.'''
#Code
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        print("Area of the shape: 0")


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        area = self.length ** 2
        print("Area of the square:", area)


# Example usage
shape = Shape()
shape.area()    # Output: Area of the shape: 0

square = Square(5)
square.area()   # Output: Area of the square: 25

#Output
'''
Area of the shape: 0
Area of the square: 25
'''
