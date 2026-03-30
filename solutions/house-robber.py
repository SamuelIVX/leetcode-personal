 # Problem: House Robber
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/house-robber/
 # Tags: Array, Dynamic Programming

class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n == 0: return 0
        elif n == 1: return nums[0]
        elif n == 2: return max(nums[0], nums[1])

        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])

        return dp[n]
