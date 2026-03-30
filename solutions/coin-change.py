 # Problem: Coin Change
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/coin-change/
 # Tags: Array, Dynamic Programming, Breadth-First Search

class Solution(object):
    def coinChange(self, coins, amount):

        if amount < 0: return -1

        total = 0 
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        
        return -1 if dp[amount] == float('inf') else dp[amount]
