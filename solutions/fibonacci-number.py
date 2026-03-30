 # Problem: Fibonacci Number
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/fibonacci-number/
 # Tags: Math, Dynamic Programming, Recursion, Memoization

class Solution(object):
    # Tabulation (bottom-up approach)
    def fib(self, n):
        if n <= 1: return n
        
        dp = [0] * (n+1)

        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
