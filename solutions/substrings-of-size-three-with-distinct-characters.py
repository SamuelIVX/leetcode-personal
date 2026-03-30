 # Problem: Substrings of Size Three with Distinct Characters
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
 # Tags: Hash Table, String, Sliding Window, Counting

class Solution(object):
    def countGoodSubstrings(self, s):
        l, r = 0,0
        valid = 0
        window = set()

        while r < len(s):
            if s[r] not in window:
                window.add(s[r])
                r += 1
            else:
                window.clear()
                l+=1
                r = l

            if len(window) == 3:
                valid += 1
                window.remove(s[l])
                l += 1

        return valid
