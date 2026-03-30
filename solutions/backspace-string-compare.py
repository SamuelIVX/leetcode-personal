 # Problem: Backspace String Compare
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/backspace-string-compare/
 # Tags: Two Pointers, String, Stack, Simulation

class Solution(object):
    def backspaceCompare(self, s, t):
        s_stack = []
        t_stack = []
        for char in s:
            if char == "#":
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(char)

        for char in t:
            if char == "#":
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(char)
        return s_stack == t_stack

        
