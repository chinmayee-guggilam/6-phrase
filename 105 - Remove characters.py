'''Please write a program which accepts a string from console and print the 
characters that have even indexes.
Example: If the following string is given as input to the program:
H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:
Helloworld'''
#Code
# Read input string from console
input_string = input("Enter a string: ")

# Iterate over characters with even indexes and print them
result = ''
for index, char in enumerate(input_string):
    if index % 2 == 0:
        result += char

# Print the result
print(result)
