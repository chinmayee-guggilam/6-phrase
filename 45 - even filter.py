'''Write a program which can filter() to make a list whose elements are even 
number between 1 and 20 (both included).'''
#Code
# Use filter() to select only the even numbers between 1 and 20
even_numbers = filter(lambda x: x % 2 == 0, range(1, 21))

# Create a list from the filtered even numbers
even_list = list(even_numbers)

# Print the even list
print(even_list)

#Output
'''
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

'''
