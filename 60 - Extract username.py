'''Assuming that we have some email addresses in the 
"username@companyname.com" format, please write program to print the 
user name of a given email address. Both user names and company names 
are composed of letters only.
Example: If the following email address is given as input to the program:
john@google.com
Six Phrase – mySlate – Python Session Plan
Then, the output of the program should be:
john
In case of input data being supplied to the question, it should be assumed to 
be a console input.'''
#Code
def extract_username(email):
    # Find the index of the @ symbol
    at_index = email.index('@')
    
    # Extract the substring before the @ symbol as the username
    username = email[:at_index]
    
    return username

# Prompt the user to enter an email address
email_address = input("Enter an email address: ")

# Extract the username from the email address
username = extract_username(email_address)

# Print the extracted username
print("Username:", username)

#Output
'''
Enter an email address: john@google.com
Username: john
'''
