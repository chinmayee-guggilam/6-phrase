'''Define a function which can generate a list where the values are square of 
numbers between 1 and 20 (both included). Then the function needs to 
print the last 5 elements in the list.'''
#Code
def print_last_five_squares():
    square_list = [num ** 2 for num in range(1, 21)]
    for value in square_list[-5:]:
        print(value)
print_last_five_squares()

#Output
'''256
289
324
361
400
'''
