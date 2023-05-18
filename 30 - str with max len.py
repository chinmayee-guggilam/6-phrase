'''Define a function that can accept two strings as input and print the string 
with maximum length in console. If two strings have the same length, then 
the function should print all strings line by line'''
#Code
def print_string_with_maximum_length(str1, str2):
    length1 = len(str1)
    length2 = len(str2)

    if length1 > length2:
        print(str1)
    elif length2 > length1:
        print(str2)
    else:
        print(str1)
        print(str2)


# Test the function
s=input('Enter 1st string:')
q=input('Enter 2nd string:')
print_string_with_maximum_length(s,q)

#Output
'''Enter 1st string:hello
Enter 2nd string:string
string'''
