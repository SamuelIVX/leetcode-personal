 # Problem: Count Number of Maximum Bitwise-OR Subsets
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
 # Tags: Array, Backtracking, Bit Manipulation, Enumeration

import functools
import operator
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        res, curOr = 0,0

        maxOr = functools.reduce(operator.or_, nums)

        def backtrack(i, curOr, maxOr):
            nonlocal res
            if i == n:
                if curOr == maxOr: res += 1
                return

            backtrack(i + 1, curOr, maxOr)

            backtrack(i + 1, curOr | nums[i], maxOr)

        backtrack(0, curOr, maxOr)
        return res
