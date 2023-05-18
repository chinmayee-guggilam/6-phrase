'''Please write a program to randomly generate a list with 5 numbers, which 
are divisible by 5 and 7 , between 1 and 1000 inclusive.'''
#Code
import random

random_numbers = []

while len(random_numbers) < 5:
    number = random.randint(1, 1000)
    if number % 5 == 0 and number % 7 == 0:
        random_numbers.append(number)

print(random_numbers)

#Output
'''
[35, 210, 245, 735, 840]
'''
