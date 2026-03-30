 # Problem: Majority Element
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/majority-element/
 # Tags: Array, Hash Table, Divide and Conquer, Sorting, Counting

class Solution(object):
    def majorityElement(self, nums):
        freq = {}
        res = float('-inf')

        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1

            if freq[n] > len(nums)/2:
                res = max(res, n)

        return res
