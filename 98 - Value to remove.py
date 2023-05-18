'''By using list comprehension, please write a program to print the list after 
removing the value 24 in [12,24,35,24,88,120,155]'''
#Code
numbers = [12, 24, 35, 24, 88, 120, 155]
value_to_remove = 24

result = [num for num in numbers if num != value_to_remove]

print(result)

#Output
'''
[12, 35, 88, 120, 155]
'''
