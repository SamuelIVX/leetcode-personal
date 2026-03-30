 # Problem: Make The String Great
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/make-the-string-great/
 # Tags: String, Stack

class Solution(object):
    def makeGood(self, s):
        stack = []
        for char in s:
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
