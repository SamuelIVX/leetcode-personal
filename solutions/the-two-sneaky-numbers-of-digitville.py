 # Problem: The Two Sneaky Numbers of Digitville
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/
 # Tags: Array, Hash Table, Math

class Solution(object):
    def getSneakyNumbers(self, nums):
        counter = {}
        for n in nums:
            if n not in counter:
                counter[n] = 0
            counter[n] += 1

        res = []
        for key, value in counter.items():
            if value == 2: res.append(key)
        return res
