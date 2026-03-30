 # Problem: Permutations
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/permutations/
 # Tags: Array, Backtracking

class Solution(object):
    def permute(self, nums):
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return

            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack(i + 1)
                    sol.pop()
        
        backtrack(0)
        return res
        
