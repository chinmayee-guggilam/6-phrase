'''Write a program which accepts a sequence of words separated by 
whitespace as input to print the words composed of digits only.
Example: If the following words is given as input to the program:
2 cats and 3 dogs.
Then, the output of the program should be:
['2', '3']
In case of input data being supplied to the question, it should be assumed to 
be a console input.'''
#Code
def extract_digit_words(sequence):
    words = sequence.split()

    digit_words = [word for word in words if word.isdigit()]

    return digit_words

# Prompt the user to enter a sequence of words
sequence = input("Enter a sequence of words: ")

# Extract the words composed of digits only
digit_words = extract_digit_words(sequence)

# Print the extracted digit words
print(digit_words)

#Output
'''
Enter a sequence of words: 2 cats and 3 dogs
['2', '3']
'''
