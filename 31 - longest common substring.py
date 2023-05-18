'''Longest Common Substring'''
#Code
def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)

    # Initialize a matrix to store the lengths of common substrings
    # where dp[i][j] represents the length of common substring ending at str1[i-1] and str2[j-1]
    dp = [[0] * (n+1) for _ in range(m+1)]

    # Variables to keep track of the length and ending index of the longest common substring
    longest_length = 0
    longest_ending_index = 0

    # Calculate the lengths of common substrings
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > longest_length:
                    longest_length = dp[i][j]
                    longest_ending_index = i

    # Extract the longest common substring
    longest_substring = str1[longest_ending_index - longest_length: longest_ending_index]

    return longest_substring


# Test the function
str1 = input('1st string')
str2 = input('2nd string')
result = longest_common_substring(str1, str2)
print("Longest Common Substring:", result)

#Output
'''1st string abcdefg
2nd string xyzagbcd
Longest Common Substring: bcd'''
