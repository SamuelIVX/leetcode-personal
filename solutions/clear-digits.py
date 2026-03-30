 # Problem: Clear Digits
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/clear-digits/
 # Tags: String, Stack, Simulation

class Solution(object):
    def clearDigits(self, s):
        stack = []
        for char in s:
            if not(char.isdigit()):
                stack.append(char)
            if stack and char.isdigit():
                stack.pop()
        return "".join(stack)
