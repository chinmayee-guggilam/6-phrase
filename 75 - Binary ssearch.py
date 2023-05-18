'''Please write a binary search function which searches an item in a sorted 
list. The function should return the index of element to be searched in the 
list.'''
#Code
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage
sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

result = binary_search(sorted_list, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")

#Output
'''
Element 23 found at index 5
'''
