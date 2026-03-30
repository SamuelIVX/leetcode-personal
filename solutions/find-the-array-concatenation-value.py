 # Problem: Find the Array Concatenation Value
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/find-the-array-concatenation-value/
 # Tags: Array, Two Pointers, Simulation

class Solution(object):
    def findTheArrayConcVal(self, nums):
        left, right = 0, len(nums) - 1
        res = 0
        while left < right:
            num_digits = len(str(nums[right]))
            res += nums[left] * (10 ** num_digits) + nums[right]
            left += 1
            right -= 1
        if len(nums) % 2 == 1: return res + nums[len(nums)//2]
        else: return res
