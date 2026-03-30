 # Problem: Find All Numbers Disappeared in an Array
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
 # Tags: Array, Hash Table

class Solution(object):
    def findDisappearedNumbers(self, nums):
        # set_nums = set(nums)
        # values = []
        # for i in range(1, len(nums)+1):
        #     if i not in set_nums:
        #         values.append(i)
        # return values
        nums_set = set(nums)  # Convert nums to a set for O(1) lookup
        return [i for i in range(1, len(nums) + 1) if i not in nums_set]
        
