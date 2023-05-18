'''Write a program which accepts a string as input to print "Yes" if the string is 
"yes" or "YES" or "Yes", otherwise print "No" '''
#Code
user_input = input("Enter a string: ")

# Convert the input string to lowercase for case-insensitive comparison
lowercase_input = user_input.lower()

# Check if the lowercase input matches "yes"
if lowercase_input == "yes":
    print("Yes")
else:
    print("No")

#Output
'''
Enter a string: Hello
No
'''
