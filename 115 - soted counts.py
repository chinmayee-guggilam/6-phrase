'''You are given a string.Your task is to count the frequency of letters of the 
string and print the letters in descending order of frequency.
If the following string is given as input to the program:
aabbbccde
Then, the output of the program should be:
b 3
a 2
c 2'''
#Code
# Get the input string
string = input()

# Initialize an empty dictionary to store letter frequencies
letter_counts = {}

# Count the frequency of each letter
for letter in string:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

# Sort the letter frequencies in descending order
sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

# Output the letters and their frequencies
for letter, count in sorted_counts:
    print(letter, count)
