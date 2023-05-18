'''You are given an integer, N. Your task is to print an alphabet rangoli of 
size N. (Rangoli is a form of Indian folk art based on creation of patterns.)
Different sizes of alphabet rangoli are shown below:
#size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
#size 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------'''
#Code
def print_rangoli(size):
    # Create a list of alphabets
    alphabets = [chr(ord('a') + i) for i in range(size)]

    # Calculate the width of the rangoli
    width = 4 * size - 3

    # Print the top half of the rangoli
    for i in range(size - 1, -1, -1):
        row = '-'.join(alphabets[i:size])
        print(row.center(width, '-'))

    # Print the bottom half of the rangoli
    for i in range(1, size):
        row = '-'.join(alphabets[i:size])
        print(row.center(width, '-'))

# Get the input size from the user
size = int(input("Enter the size of the rangoli: "))

# Print the alphabet rangoli
print_rangoli(size)
