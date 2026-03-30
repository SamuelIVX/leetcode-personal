 # Problem: Valid Parentheses
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/valid-parentheses/
 # Tags: String, Stack

class Solution(object):
    def isValid(self, s):
        if len(s) % 2 == 1:
            return False
        stack = []
        hash = {')' : '(', ']' : '[', '}' : '{'}
        for i in s:
            if i in hash:
                if stack and stack[-1] == hash[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack

