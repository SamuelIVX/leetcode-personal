 # Problem: Score of a String
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/score-of-a-string/
 # Tags: String

class Solution(object):
    def scoreOfString(self, s):
        l, sum = 0,0

        for r in range(1, len(s)):
            sum += abs(ord(s[l]) - ord(s[r]))
            l += 1
        return sum
        
