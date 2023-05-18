'''Please write a program using generator to print the numbers which can be 
divisible by 5 and 7 between 0 and n in comma separated form while n is 
input by console.
Example: If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70
In case of input data being supplied to the question, it should be assumed to 
be a console input.'''
#Code
def divisible_by_5_and_7(n):
    for i in range(n + 1):
        if i % 5 == 0 and i % 7 == 0:
            yield i

n = int(input("Enter a value for n: "))  # Prompt the user to enter the value of n

divisible_nums = divisible_by_5_and_7(n)  # Create a generator object

result = ', '.join(map(str, divisible_nums))  # Join the divisible numbers with commas

print("Numbers divisible by 5 and 7:", result)

#Output
'''
Enter a value for n: 100
Numbers divisible by 5 and 7: 0, 35, 70
'''
