#!/usr/bin/python3

def makeChange(coins, total):
    if total < 0:
        return 0  # No need to make any change for a negative total
    if total == 0:
        return 0  # No coins needed for total of 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins needed for amount 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
