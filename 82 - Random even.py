'''Please write a program to randomly generate a list with 5 even numbers 
between 100 and 200 inclusive.'''
#Code
import random

random_numbers = random.sample(range(100, 201, 2), 5)
print(random_numbers)

#Output
'''
[122, 142, 186, 178, 162]
'''
