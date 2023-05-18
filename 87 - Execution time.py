'''Please write a program to print the running time of execution of "1+1" for 
100 times'''
#Code
import timeit

# Define the code to be executed
code = "1 + 1"

# Measure the execution time
execution_time = timeit.timeit(code, number=100)

# Print the execution time
print("Execution time:", execution_time)
