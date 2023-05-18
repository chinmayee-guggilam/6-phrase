'''Subset Sum Problem'''
#Code
def is_subset_sum(nums, target_sum):
    n = len(nums)
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if j < nums[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

    return dp[n][target_sum]

# Example usage
nums = [3, 7, 4, 2, 8]
target_sum = 10

if is_subset_sum(nums, target_sum):
    print("Subset with the target sum exists")
else:
    print("No subset with the target sum exists")

#Output
'''
Subset with the target sum exists
'''
