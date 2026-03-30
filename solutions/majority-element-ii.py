 # Problem: Majority Element II
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/majority-element-ii/
 # Tags: Array, Hash Table, Sorting, Counting

class Solution(object):
    def majorityElement(self, nums):
        count = {}
        size = len(nums)
        
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        
        return [key for key, value in count.items() if value > size/3]
