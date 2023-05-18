'''Define a function which can generate a list where the values are square of 
numbers between 1 and 20 (both included). Then the function needs to 
print all values except the first 5 elements in the list.'''
#Code
def print_values_except_first_five():
    square_list = [num ** 2 for num in range(1, 21)]
    for value in square_list[5:]:
        print(value)
print_values_except_first_five()

#Output
'''36
49
64
...
361
400
'''
