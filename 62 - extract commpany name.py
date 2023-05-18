'''Assuming that we have some email addresses in the 
"username@companyname.com" format, please write program to print the 
company name of a given email address. Both user names and company 
names are composed of letters only.
Example: If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
google
In case of input data being supplied to the question, it should be assumed to 
be a console input.'''
#Code
def extract_company_name(email):
    # Find the index of the @ symbol
    at_index = email.index('@')

    # Find the index of the dot after the @ symbol
    dot_index = email.index('.', at_index)

    # Extract the substring between the @ symbol and the dot as the company name
    company_name = email[at_index + 1:dot_index]

    return company_name

# Prompt the user to enter an email address
email_address = input("Enter an email address: ")

# Extract the company name from the email address
company_name = extract_company_name(email_address)

# Print the extracted company name
print("Company Name:", company_name)

#Output
'''
Enter an email address: john@google.com
Company Name: google
'''
