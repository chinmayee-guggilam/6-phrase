'''With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first 
half values in one line and the last half values in one line'''
#Code
values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Find the index to split the tuple into two halves
split_index = len(values) // 2

# Print the first half of the values in one line
first_half = values[:split_index]
print(*first_half, sep=' ', end='\n')

# Print the last half of the values in another line
last_half = values[split_index:]
print(*last_half, sep=' ')

#Output
'''
1 2 3 4 5
6 7 8 9 10
'''
