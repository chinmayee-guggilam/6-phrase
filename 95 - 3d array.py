'''By using list comprehension, please write a program generate a 3*5*8 3D 
array whose each element is 0.'''
#code
array_3d = [[[0 for _ in range(8)] for _ in range(5)] for _ in range(3)]

# Print the 3D array
for i in range(3):
    for j in range(5):
        print(array_3d[i][j])
    print()
