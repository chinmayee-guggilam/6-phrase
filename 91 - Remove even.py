'''Please write a program to print the list after removing even numbers in 
[5,6,77,45,22,12,24]'''
#Code
def remove_even_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

# Test the function
numbers = [5, 6, 77, 45, 22, 12, 24]
result = remove_even_numbers(numbers)
print("List after removing even numbers:", result)
