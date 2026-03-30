 # Problem: Count Pairs Whose Sum is Less than Target
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/
 # Tags: Array, Two Pointers, Binary Search, Sorting

class Solution(object):
    def countPairs(self, nums, target):
        pairs = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                pairs += 1
            right -= 1
            if right <= left:
                left += 1
                right = len(nums) - 1
        return pairs
