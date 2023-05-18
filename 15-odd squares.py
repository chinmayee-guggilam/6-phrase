'''Use a list comprehension to square each odd number in a list. The list is
input by a sequence of comma-separated numbers. Suppose the following
input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,9,25,49,81'''
#Code:
numbers = input("Type in: ")
odd_list = [i for i in numbers.split(',') if (int(i) % 2 != 0)]
for i in odd_list:
    print(int(i)*int(i),end=',')
#Output:
'''Type in: 1,2,3,4,5,6,7,8,9
1,9,25,49,81,'''
