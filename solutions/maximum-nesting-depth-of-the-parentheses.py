 # Problem: Maximum Nesting Depth of the Parentheses
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
 # Tags: String, Stack

class Solution(object):
    def maxDepth(self, s):
        stack = []
        maxDepth = 0
        for char in s:
            if char == ")":
                if stack:
                    stack.pop()
            elif char == "(":
                stack.append(char)
                currentDepth = len(stack)
                maxDepth = max(currentDepth, maxDepth)
        return maxDepth
