'''Define a function that can accept two strings as input and concatenate 
them and then print it in console.'''
#Code
def concatenate_strings(str1, str2):
    concatenated_string = str1 + str2
    print(concatenated_string)


s=input('Enter first string:')
q=input('Enter  second string:')
concatenate_strings(s,q)

#Output
'''Enter first string:Hello
Enter  second string:World
HelloWorld'''
