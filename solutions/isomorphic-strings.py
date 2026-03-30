 # Problem: Isomorphic Strings
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/isomorphic-strings/
 # Tags: Hash Table, String

class Solution(object):
    def isIsomorphic(self, s, t):
        mapping = {}
        taken = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in mapping and t[i] != mapping[s[i]] or t[i] in taken and s[i] not in mapping:
                return False
            
            mapping[s[i]] = t[i]
            taken[t[i]] = 1        

        return True 
        
