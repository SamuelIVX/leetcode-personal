 # Problem: Monotonic Array
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/monotonic-array/
 # Tags: Array

class Solution(object):
    def isMonotonic(self, nums):
        n = len(nums)
        if n <= 1:
            return True

        increasing, decreasing = True, True
        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                decreasing = False
            if nums[i] > nums[i + 1]:
                increasing = False

        return increasing | decreasing
