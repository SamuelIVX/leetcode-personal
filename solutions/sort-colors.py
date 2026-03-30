 # Problem: Sort Colors
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/sort-colors/
 # Tags: Array, Two Pointers, Sorting

class Solution(object):
    def sortColors(self, nums):
        low, mid, high = 0, 0, len(nums)-1

        while (mid <= high):
            if nums[mid] == 0:
                nums[mid],nums[low] = nums[low],nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid],nums[high] = nums[high],nums[mid]
                high -= 1


