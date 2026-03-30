 # Problem: Count Partitions with Even Sum Difference
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/count-partitions-with-even-sum-difference/
 # Tags: Array, Math, Prefix Sum

class Solution(object):
    def countPartitions(self, nums):
        leftSum = partitions = 0
        total = sum(nums)
        for current in range(len(nums)-1):
            leftSum += nums[current]
            if((leftSum - (total - leftSum)) % 2 == 0):
                partitions += 1
        return partitions
        
