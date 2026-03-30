 # Problem: Set Mismatch
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/set-mismatch/
 # Tags: Array, Hash Table, Bit Manipulation, Sorting

from collections import Counter
class Solution(object):
    def findErrorNums(self, nums):
        mymap = Counter(nums)
        res = []
        
        for key, value in mymap.items():
            if value > 1:
                res.append(key)

        set_nums = set(nums)
        for i in range(1, len(nums)+1):
            if i not in set_nums:
                res.append(i)
        
        return res
