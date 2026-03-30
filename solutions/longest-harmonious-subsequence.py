 # Problem: Longest Harmonious Subsequence
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/longest-harmonious-subsequence/
 # Tags: Array, Hash Table, Sliding Window, Sorting, Counting

class Solution(object):
    def findLHS(self, nums):
        lhs = 0
        mp = {}

        for n in nums:
            if n not in mp:
                mp[n] = 0
            mp[n] += 1

        for n in nums:
            if n+1 in mp:
                lhs = max(lhs, mp[n] + mp[n+1])

        return lhs
