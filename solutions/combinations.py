 # Problem: Combinations
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/combinations/
 # Tags: Backtracking

class Solution(object):
    def combine(self, n, k):
        res, sol = [], []

        def backtrack(i):
            if len(sol) == k:
                res.append(sol[:])
                return

            for num in range(i+1, n+1):            
                sol.append(num)
                backtrack(num)
                sol.pop()

        backtrack(0)
        return res
