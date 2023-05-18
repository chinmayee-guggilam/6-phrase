'''You are given a date. Your task is to find what the day is on that date.
Input
Six Phrase – mySlate – Python Session Plan
A single line of input containing the space separated month, day and year, 
respectively, in MM DD YYYY format.
08 05 2015
Output
Output the correct day in capital letters.
WEDNESDAY'''
#Code
import datetime

# Get the input date from the user
date_input = input("Enter the date (MM DD YYYY): ")

# Convert the input date to a datetime object
date = datetime.datetime.strptime(date_input, "%m %d %Y")

# Get the day of the week from the datetime object
day = date.strftime("%A").upper()

# Print the day
print(day)
