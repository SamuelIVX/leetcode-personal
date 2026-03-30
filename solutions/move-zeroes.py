 # Problem: Move Zeroes
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/move-zeroes/
 # Tags: Array, Two Pointers

class Solution(object):
    def moveZeroes(self, nums):
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums

