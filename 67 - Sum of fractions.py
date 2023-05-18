'''Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by 
console (n>0).
Example: If the following n is given as input to the program:
5
Then, the output of the program should be:
3.55
In case of input data being supplied to the question, it should be assumed to 
be a console input'''
#Code
n = int(input("Enter a value for n: "))  # Prompt the user to enter the value of n

sum_fractions = 0  # Initialize the sum of fractions

for i in range(1, n+1):
    sum_fractions += i / (i + 1)

print("Sum of fractions:", round(sum_fractions, 2))  # Print the sum of fractions rounded to 2 decimal places

#Output
'''
Enter a value for n: 5
Sum of fractions: 3.55
'''
