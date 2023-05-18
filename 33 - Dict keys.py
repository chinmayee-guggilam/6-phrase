'''Define a function which can generate a dictionary where the keys are 
numbers between 1 and 20 (both included) and the values are square of 
keys. The function should just print the keys only'''
#Code
def print_square_dict_keys():
    square_dict = {num: num ** 2 for num in range(1, 21)}
    for key in square_dict.keys():
        print(key)
print_square_dict_keys()

#Output
'''1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20'''
