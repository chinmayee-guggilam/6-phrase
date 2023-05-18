'''By using list comprehension, please write a program to print the list after 
removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155]'''
#Code
def remove_numbers_by_indices(numbers):
    return [num for i, num in enumerate(numbers) if i not in [0, 2, 4, 6]]

# Test the function
numbers = [12, 24, 35, 70, 88, 120, 155]
result = remove_numbers_by_indices(numbers)
print("List after removing numbers by indices:", result)
