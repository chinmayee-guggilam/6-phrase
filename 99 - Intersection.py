'''With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write 
a program to make a list whose elements are intersection of the above given 
lists.'''
#Code
list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]

intersection = [num for num in list1 if num in list2]

print(intersection)

#Output
'''
[35]
'''
