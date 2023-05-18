'''Write a program which can map() to make a list whose elements are square 
of elements in [1,2,3,4,5,6,7,8,9,10]'''
#Code
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use map() to square each element in the original list
squared_list = list(map(lambda x: x ** 2, original_list))

# Print the squared list
print(squared_list)

#Output
'''
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

'''
