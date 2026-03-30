 # Problem: Jewels and Stones
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/jewels-and-stones/
 # Tags: Hash Table, String

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        res = 0
        arr = list(jewels)
        for i in range(len(stones)):
            if stones[i] in arr: res += 1
        return res
        
