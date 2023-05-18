'''Longest Palindromic Subsequence'''
#Code
def longest_palindromic_subsequence(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        dp[i][i] = 1

        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]

# Example usage
sequence = input()
length = longest_palindromic_subsequence(sequence)
print("Length of the longest palindromic subsequence:", length)

#Output
'''
BBABCBCAB
Length of the longest palindromic subsequence: 7
'''
