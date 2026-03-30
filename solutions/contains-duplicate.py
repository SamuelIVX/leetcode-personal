 # Problem: Contains Duplicate
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/contains-duplicate/
 # Tags: Array, Hash Table, Sorting

class Solution(object):
    def containsDuplicate(self, nums):
        return (len(nums) != len(set(nums)))
        # distinctSet = set()
        # for i in range(len(nums)):
        #     if nums[i] in distinctSet:
        #         return True
        #     distinctSet.add(nums[i])
        # return False


        
