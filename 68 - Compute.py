'''Write a program to compute:
f(n)=f(n-1)+100 when n>0
and f(0)=1
with a given n input by console (n>0).
Example: If the following n is given as input to the program:
Six Phrase – mySlate – Python Session Plan
5
Then, the output of the program should be:
500
In case of input data being supplied to the question, it should be assumed to 
be a console input'''
#Code
def compute_f(n):
    if n == 0:
        return 1
    else:
        return compute_f(n - 1) + 100

n = int(input("Enter a value for n: "))  # Prompt the user to enter the value of n

result = compute_f(n)

print("Result:", result)

#Output
'''
Enter a value for n: 5
Result: 500
'''
