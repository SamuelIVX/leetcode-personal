 # Problem: Subsets
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/subsets/
 # Tags: Array, Backtracking, Bit Manipulation

class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return

            # Take the left path (don't pick nums[i])
            backtrack(i + 1)

            # Take the right path (pick nums[i])
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()
        
        backtrack(0)
        return res
