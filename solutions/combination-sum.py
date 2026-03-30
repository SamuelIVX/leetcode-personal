 # Problem: Combination Sum
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/combination-sum/
 # Tags: Array, Backtracking

class Solution(object):
    def combinationSum(self, candidates, target):
        n = len(candidates)
        res, sol = [], []

        def backtrack(i, target):
            if target < 0 or i == n:
                return
            elif target == 0:
                res.append(sol[:])
                return

            # Skip it
            backtrack(i + 1, target)

            # Take it
            sol.append(candidates[i])
            backtrack(i, target - candidates[i])
            sol.pop()
            
        backtrack(0, target)
        return res
