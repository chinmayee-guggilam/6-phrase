'''Egg Drop Problem'''
#Code
def eggDrop(e, f):
    dp = [[float('inf')] * (f + 1) for _ in range(e + 1)]

    for i in range(f + 1):
        dp[1][i] = i

    for i in range(2, e + 1):
        for j in range(1, f + 1):
            for k in range(1, j + 1):
                temp = 1 + max(dp[i - 1][k - 1], dp[i][j - k])
                dp[i][j] = min(dp[i][j], temp)

    return dp[e][f]
eggs = 2
floors = 100
result = eggDrop(eggs, floors)
print("Minimum number of attempts:", result)
