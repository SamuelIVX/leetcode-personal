 # Problem: Group Anagrams
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/group-anagrams/
 # Tags: Array, Hash Table, String, Sorting

class Solution(object):
    def groupAnagrams(self, strs):
        res = {}

        for s in strs:
            k = "".join(sorted(s))
            if k not in res:
                res[k] = []
            res[k].append(s)

        return [val for val in res.values()]
