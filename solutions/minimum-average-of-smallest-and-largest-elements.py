 # Problem: Minimum Average of Smallest and Largest Elements
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/
 # Tags: Array, Two Pointers, Sorting

class Solution(object):
    def minimumAverage(self, nums):
        nums.sort()
        left = 0
        res = []
        right = len(nums) - 1
        while left < right:
            avg = (nums[left] + nums[right] + 0.0) / 2
            res.append(avg)
            left += 1
            right -= 1
        return min(res)

