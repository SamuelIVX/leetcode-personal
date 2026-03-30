 # Problem: Sum of All Subset XOR Totals
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/sum-of-all-subset-xor-totals/
 # Tags: Array, Math, Backtracking, Bit Manipulation, Combinatorics, Enumeration

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        res, curXOR = 0, 0

        def backtrack(i, curXOR):
            nonlocal res
            if i == n:
                res += curXOR
                return

            backtrack(i + 1, curXOR)

            backtrack(i + 1, curXOR ^ nums[i])
        
        backtrack(0, curXOR)
        return res
