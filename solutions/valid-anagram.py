 # Problem: Valid Anagram
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/valid-anagram/
 # Tags: Hash Table, String, Sorting

class Solution(object):
    def isAnagram(self, s, t):
        mp1 = {}
        mp2 = {}

        for c in s:
            if c not in mp1:
                mp1[c] = 0
            mp1[c] += 1
        
        for c in t:
            if c not in mp2:
                mp2[c] = 0
            mp2[c] += 1
        
        return mp1 == mp2
