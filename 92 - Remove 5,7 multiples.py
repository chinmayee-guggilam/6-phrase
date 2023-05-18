'''By using list comprehension, please write a program to print the list after 
removing numbers which are divisible by 5 and 7 in 
[12,24,35,70,88,120,155]'''
#code
def remove_numbers_divisible_by_5_and_7(numbers):
    return [num for num in numbers if num % 5 != 0 or num % 7 != 0]

# Test the function
numbers = [12, 24, 35, 70, 88, 120, 155]
result = remove_numbers_divisible_by_5_and_7(numbers)
print("List after removing numbers divisible by 5 and 7:", result)
