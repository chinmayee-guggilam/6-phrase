'''The Fibonacci Sequence is computed based on the following formula:
 f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by 
console.
Example: If the following n is given as input to the program:
7
Then, the output of the program should be:
0,1,1,2,3,5,8,13
In case of input data being supplied to the question, it should be assumed to 
be a console input.'''
#Code
n = int(input("Enter a value for n: "))  # Prompt the user to enter the value of n

fibonacci_sequence = [0, 1]  # Initialize the Fibonacci sequence with the first two numbers

# Calculate the Fibonacci sequence up to n
for i in range(2, n+1):
    fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])

# Print the Fibonacci sequence
print("Fibonacci sequence:", ', '.join(map(str, fibonacci_sequence)))

#Output'
'''
Enter a value for n: 7
Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13
'''
