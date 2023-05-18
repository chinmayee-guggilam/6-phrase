'''Define a function which can generate and print a tuple where the value are 
square of numbers between 1 and 20 (both included).'''
#Code
def print_square_tuple():
    square_tuple = tuple(num ** 2 for num in range(1, 21))
    print(square_tuple)
print_square_tuple()

#Output
'''(1, 4, 9, ..., 361, 400)
'''
