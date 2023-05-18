'''Please write a program using generator to print the even numbers between 
0 and n in comma separated form while n is input by console.
Example: If the following n is given as input to the program:
10
Then, the output of the program should be:
0,2,4,6,8,10
In case of input data being supplied to the question, it should be assumed to 
be a console input.'''
#Code
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a value for n: "))  # Prompt the user to enter the value of n

even_nums = even_numbers(n)  # Create a generator object

result = ', '.join(map(str, even_nums))  # Join the even numbers with commas

print("Even numbers:", result)

#Output
'''
Enter a value for n: 10
Even numbers: 0, 2, 4, 6, 8, 10
'''
