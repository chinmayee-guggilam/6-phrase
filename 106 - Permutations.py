'''Please write a program which prints all permutations of [1,2,3]'''
#Code
from itertools import permutations

# Define the input list
input_list = [1, 2, 3]

# Generate all permutations
permutations_list = list(permutations(input_list))

# Print each permutation
for permutation in permutations_list:
    print(permutation)

#Output
'''
(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)
'''
