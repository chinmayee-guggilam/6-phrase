'''Please write a program to output a random even number between 0 and 10 
inclusive using random module and list comprehension'''
#Code
import random

random_even = random.choice([num for num in range(0, 11) if num % 2 == 0])
print(random_even)

#Output
'''
6
'''
