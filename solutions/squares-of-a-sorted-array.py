 # Problem: Squares of a Sorted Array
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/squares-of-a-sorted-array/
 # Tags: Array, Two Pointers, Sorting

class Solution(object):
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums
