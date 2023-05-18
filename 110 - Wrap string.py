'''You are given a string S and width W. Your task is to wrap the string into a 
paragraph of width.
If the following string is given as input to the program:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Then, the output of the program should be:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ'''
#Code
def wrap_text(string, width):
    wrapped_text = ""
    for i in range(0, len(string), width):
        wrapped_text += string[i:i+width] + "\n"
    return wrapped_text

# Get the input string and width from the user
string = input("Enter the string: ")
width = int(input("Enter the width: "))

# Wrap the string into paragraphs of the given width
wrapped_string = wrap_text(string, width)

# Print the wrapped string
print(wrapped_string)
