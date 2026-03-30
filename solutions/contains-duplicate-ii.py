 # Problem: Contains Duplicate II
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/contains-duplicate-ii/
 # Tags: Array, Hash Table, Sliding Window

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)

        counter = {}
        
        for i in range(n):
            if nums[i] in counter and abs(i - counter[nums[i]]) <= k:
                return True
            counter[nums[i]] = i
        return False
        
