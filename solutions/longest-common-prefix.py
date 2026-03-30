 # Problem: Longest Common Prefix
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/longest-common-prefix/
 # Tags: Array, String, Trie

class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix
        
