 # Problem: Count Substrings That Satisfy K-Constraint I
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/
 # Tags: String, Sliding Window

class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        count0, count1 = 0,0
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] == '0':
                count0 += 1
            else:
                count1 += 1

            while count0 > k and count1 > k:
                if s[l] == '0': count0 -= 1
                else: count1 -= 1
                l += 1

            res += (r - l) + 1

        return res 
