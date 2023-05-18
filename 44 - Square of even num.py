'''Write a program which can map() and filter() to make a list whose elements 
are square of even number in [1,2,3,4,5,6,7,8,9,10].'''
#Code
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter() to select only the even numbers from the original list
even_numbers = filter(lambda x: x % 2 == 0, original_list)

# Use map() to square each even number
squared_list = list(map(lambda x: x ** 2, even_numbers))

# Print the squared list
print(squared_list)

#Output
'''
[4, 16, 36, 64, 100]

'''
