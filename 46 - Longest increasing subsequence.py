'''Longest Increasing Subsequence'''
#Code
def longest_increasing_subsequence(nums):
    n = len(nums)
    lis = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    return max(lis)

# Example usage
sequence = list(map(int,input().split()))
length = longest_increasing_subsequence(sequence)
print("Length of the longest increasing subsequence:", length)

#Output
'''
[10, 22, 9, 33, 21, 50, 41, 60]
Length of the longest increasing subsequence: 5

'''
