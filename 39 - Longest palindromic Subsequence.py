'''Longest Palindromic Subsequence'''
#Code
def longest_palindromic_subsequence(s):
    n = len(s)
    # Create a table to store the lengths of LPS for different subproblems
    lps = [[0] * n for _ in range(n)]

    # All individual characters are palindromic subsequences of length 1
    for i in range(n):
        lps[i][i] = 1

    # Loop to consider all subsequence lengths from 2 to n
    for subseq_len in range(2, n + 1):
        for i in range(n - subseq_len + 1):
            j = i + subseq_len - 1
            if s[i] == s[j] and subseq_len == 2:
                # Case when there are only 2 characters and both are the same
                lps[i][j] = 2
            elif s[i] == s[j]:
                # Characters at both ends are the same
                lps[i][j] = lps[i + 1][j - 1] + 2
            else:
                # Characters at both ends are different
                lps[i][j] = max(lps[i][j - 1], lps[i + 1][j])

    # Length of the longest palindromic subsequence
    return lps[0][n - 1]

s = input()
length = longest_palindromic_subsequence(s)
print("Length of the longest palindromic subsequence:", length)

#Output
'''
abcbda
Length of the longest palindromic subsequence: 5
'''
