 # Problem: Merge Strings Alternately
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/merge-strings-alternately/
 # Tags: Two Pointers, String

class Solution(object):
    def mergeAlternately(self, word1, word2):
        res = []
        n1, n2 = len(word1), len(word2)
        for i in range(max(n1, n2)):
            if i < n1 and i < n2:
                res.append(word1[i])
                res.append(word2[i])
            elif i >= n2:
                res.append(word1[i])
            elif i >= n1:
                res.append(word2[i])
        return "".join(res)
