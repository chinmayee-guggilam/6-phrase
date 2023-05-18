'''Kadane’s Algorithm'''
#Code
def kadanes_algorithm(nums):
    max_sum = float('-inf')  # Initialize maximum sum as negative infinity
    current_sum = 0  # Initialize current sum as 0

    for num in nums:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0

    return max_sum

# Example usage
array = [-2, -3, 4, -1, -2, 1, 5, -3]
max_sum = kadanes_algorithm(array)
print("Maximum sum of a subarray:", max_sum)

#Output
'''
Maximum sum of a subarray: 7
'''
