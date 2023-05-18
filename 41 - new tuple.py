'''Write a program to generate and print another tuple whose values are even 
numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).'''
#Code
original_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Generate a new tuple with even numbers from the original tuple
even_tuple = tuple(num for num in original_tuple if num % 2 == 0)

# Print the even tuple
print(even_tuple)

#Output
'''
(2, 4, 6, 8, 10)
'''
