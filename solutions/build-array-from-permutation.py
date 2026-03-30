 # Problem: Build Array from Permutation
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/build-array-from-permutation/
 # Tags: Array, Simulation

class Solution(object):
    def buildArray(self, nums):
        return [nums[n] for n in nums]
        
