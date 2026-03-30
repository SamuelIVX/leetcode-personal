 # Problem: Two Sum
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/two-sum/
 # Tags: Array, Hash Table

class Solution(object):
    def twoSum(self, nums, target):
        mp = {}

        for index, num in enumerate(nums):
            if target - num in mp:
                return [mp[target-num], index]
            mp[num] = index
