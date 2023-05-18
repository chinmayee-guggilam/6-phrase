'''Please write a program to output a random number, which is divisible by 5 
and 7, between 10 and 150 inclusive using random module and list 
comprehension'''
#Code
import random

random_number = random.choice([num for num in range(10, 151) if num % 5 == 0 and num % 7 == 0])
print(random_number)

#Output
'''
105
'''
