'''The coin change Problem'''
#Code
def coin_change(coins, amount):
    # Create a table to store the minimum number of coins needed for each amount
    dp = [float('inf')] * (amount + 1)

    # Base case: 0 coins needed to make amount 0
    dp[0] = 0

    # Iterate over all amounts from 1 to the target amount
    for i in range(1, amount + 1):
        # Try all possible coin denominations
        for coin in coins:
            # Check if the coin denomination is less than or equal to the current amount
            if coin <= i:
                # Update the minimum number of coins needed for the current amount
                dp[i] = min(dp[i], 1 + dp[i - coin])

    # Return the minimum number of coins needed for the target amount
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
coins = [1, 2, 5]
amount = 11

minimum_coins = coin_change(coins, amount)
print("Minimum number of coins:", minimum_coins)

#Output
'''
Minimum number of coins: 3
'''
