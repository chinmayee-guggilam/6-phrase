'''By using list comprehension, please write a program to print the list after 
removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155]'''
#Code
numbers = [12, 24, 35, 70, 88, 120, 155]
indices_to_remove = [0, 4, 5]

result = [num for i, num in enumerate(numbers) if i not in indices_to_remove]

print(result)

#Output
'''
[24, 35, 70, 155]
'''
