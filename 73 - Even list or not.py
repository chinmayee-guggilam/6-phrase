'''Please write assert statements to verify that every number in the list
[2,4,6,8] is even.'''
#Code
numbers = [2, 4, 6, 8]

for num in numbers:
    assert num % 2 == 0, f"{num} is not an even number"

print("All numbers are even")

#Output
