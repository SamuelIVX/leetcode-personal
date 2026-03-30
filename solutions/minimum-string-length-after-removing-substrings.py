 # Problem: Minimum String Length After Removing Substrings
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/minimum-string-length-after-removing-substrings/
 # Tags: String, Stack, Simulation

class Solution(object):
    def minLength(self, s):
        stack = []
        for c in s:
            if stack and (
                (c == 'B' and stack[-1] == 'A') or 
                (c == 'D' and stack[-1] == 'C')):
                    stack.pop()
            else: 
                stack.append(c)
        return len(stack)

