'''Please write a program which count and print the numbers of each 
character in a string input by console.
Example: If the following string is given as input to the program:
abcdefgabc
Then, the output of the program should be:
a,2
c,2
b,2
e,1
d,1
g,1
f,1'''
#Code
def count_characters(string):
    char_count = {}

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char, count in char_count.items():
        print(char + ',' + str(count))

# Read input string from console
input_string = input("Enter a string: ")

# Call the count_characters function
count_characters(input_string)

#Output
'''
a,2
b,2
c,2
d,1
e,1
f,1
g,1
'''
