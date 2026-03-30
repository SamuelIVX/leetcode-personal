 # Problem: Remove All Occurrences of a Substring
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/remove-all-occurrences-of-a-substring/
 # Tags: String, Stack, Simulation

class Solution(object):
    def removeOccurrences(self, s, part):
        stack = []

        for c in s:
            stack.append(c)
            while stack and "".join(stack[-len(part):]) == part:
                stack = stack[:-len(part)]
        return "".join(stack)
        
