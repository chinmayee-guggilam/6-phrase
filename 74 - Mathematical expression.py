'''Please write a program which accepts basic mathematic expression from 
console and print the evaluation result.
Example: If the following n is given as input to the program:
35 + 3
Then, the output of the program should be:
38'''
#Code
expression = input("Enter a mathematical expression: ")

result = eval(expression)

print("Evaluation result:", result)

#Output
'''
Enter a mathematical expression: 35 + 3
Evaluation result: 38
'''
