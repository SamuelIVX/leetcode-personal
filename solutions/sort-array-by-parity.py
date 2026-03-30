 # Problem: Sort Array By Parity
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/sort-array-by-parity/
 # Tags: Array, Two Pointers, Sorting

class Solution(object):
    def sortArrayByParity(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] % 2 == 1 and nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] % 2 == 0:
                left += 1
            if nums[right] % 2 == 1:
                right -= 1
        return nums
