'''Write a program to read an ASCII string and to convert it to a unicode string 
encoded by utf-8.'''
#Code
# Read the ASCII string
ascii_string = input("Enter an ASCII string: ")

# Convert the ASCII string to a Unicode string encoded by UTF-8
unicode_string = ascii_string.encode("utf-8")

# Print the Unicode string
print("Unicode string (UTF-8):", unicode_string)

#Output
'''
Enter an ASCII string: hello
Unicode string (UTF-8): b'hello'
'''
