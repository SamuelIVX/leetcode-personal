 # Problem: Longest Substring Without Repeating Characters
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
 # Tags: Hash Table, String, Sliding Window

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        window = set()
        l, res = 0, 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            res = max(res, r - l + 1)

        return res
