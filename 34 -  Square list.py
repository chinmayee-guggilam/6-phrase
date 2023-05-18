'''Define a function which can generate and print a list where the values are 
square of numbers between 1 and 20 (both included).'''
#Code
def print_square_list():
    square_list = [num ** 2 for num in range(1, 21)]
    for value in square_list:
        print(value)
print_square_list()

#Output
'''1
4
9
16
25
36
49
64
81
100
121
144
169
196
225
256
289
324
361
400'''
