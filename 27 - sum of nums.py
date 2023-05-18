'''Define a function that can receive two integer numbers in string form and 
compute their sum and then print it in console.'''
#Code
def compute_and_print_sum(num1, num2):
    sum_result = int(num1) + int(num2)
    print("Sum:", sum_result)

n=input()
m=input()
compute_and_print_sum(n,m)

#Output
'''10
20
Sum: 30'''
