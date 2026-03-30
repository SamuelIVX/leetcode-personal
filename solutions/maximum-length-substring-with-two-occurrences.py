 # Problem: Maximum Length Substring With Two Occurrences
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/
 # Tags: Hash Table, String, Sliding Window

class Solution(object):
    def maximumLengthSubstring(self, s):
        mapp = {}
        longest = l = 0

        for r in range(len(s)):
            if s[r] not in mapp: mapp[s[r]] = 0
            mapp[s[r]] += 1

            while mapp[s[r]] > 2:
                mapp[s[l]] -= 1
                l += 1
        
            longest = max(longest, r - l + 1)

        return longest    
