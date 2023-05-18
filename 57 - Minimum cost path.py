'''Minimum Cost Path'''
#Code
def min_cost_path(cost_grid, m, n):
    dp = [[0] * n for _ in range(m)]

    dp[0][0] = cost_grid[0][0]

    # Initialize the first column
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + cost_grid[i][0]

    # Initialize the first row
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + cost_grid[0][j]

    # Fill in the remaining cells
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = cost_grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[m - 1][n - 1]


# Example usage
cost_grid = [
    [1, 3, 5, 8],
    [4, 2, 1, 7],
    [4, 3, 2, 3]
]

m = len(cost_grid)
n = len(cost_grid[0])

minimum_cost = min_cost_path(cost_grid, m, n)
print("Minimum cost path:", minimum_cost)


#Output
'''
Minimum cost path: 13
'''
