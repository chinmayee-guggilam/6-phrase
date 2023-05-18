'''Given 2 sets of integers, M and N, print their symmetric difference in 
ascending order. The term symmetric difference indicates those values that 
exist in either M or N but do not exist in both.
Input
The first line of input contains an integer, M.The second line contains M 
space-separated integers.The third line contains an integer, N.The fourth 
line contains N space-separated integers.
4
2 4 5 9
4
2 4 11 12
Output
Output the symmetric difference integers in ascending order, one per line.
5
9
11
12'''
#Code
# Get the input for set M
m = int(input())
set_m = set(map(int, input().split()))

# Get the input for set N
n = int(input())
set_n = set(map(int, input().split()))

# Find the symmetric difference
symmetric_diff = set_m.symmetric_difference(set_n)

# Sort the symmetric difference in ascending order
sorted_diff = sorted(symmetric_diff)

# Print the symmetric difference
for num in sorted_diff:
    print(num)

