'''Write a program which can map() to make a list whose elements are square 
of numbers between 1 and 20 (both included).'''
#Code
# Use map() to square each number between 1 and 20
squared_list = list(map(lambda x: x ** 2, range(1, 21)))

# Print the squared list
print(squared_list)

#Output
'''
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]

'''
