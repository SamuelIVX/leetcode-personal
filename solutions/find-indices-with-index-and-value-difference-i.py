 # Problem: Find Indices With Index and Value Difference I
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/
 # Tags: Array, Two Pointers

class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if ((abs(i - j) >= indexDifference) and (abs(nums[i] - nums[j]) >= valueDifference)):
                     return [i, j]
        return [-1, -1]
