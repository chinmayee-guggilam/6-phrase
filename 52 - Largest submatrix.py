'''Find the largest kxk submatrix with all entries 1 in a mxn binary matrix'''
#Code
def largest_submatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])

    # Create a new matrix to store the intermediate results
    dp = [[0] * n for _ in range(m)]

    # Copy the first row and first column from the original matrix to dp
    for i in range(m):
        dp[i][0] = matrix[i][0]

    for j in range(n):
        dp[0][j] = matrix[0][j]

    # Calculate the size of the largest submatrix
    max_size = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 1:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_size = max(max_size, dp[i][j])

    return max_size


# Example usage
binary_matrix = [
    [1, 1, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1],
    [1, 0, 0, 1, 1]
]

size = largest_submatrix(binary_matrix)
print("Size of the largest submatrix with all entries as 1:", size)

#Output
'''
Size of the largest submatrix with all entries as 1: 3
'''
