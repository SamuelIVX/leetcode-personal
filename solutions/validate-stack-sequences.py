 # Problem: Validate Stack Sequences
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/validate-stack-sequences/
 # Tags: Array, Stack, Simulation

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        stack = []
        j = 0

        for i in pushed:
            stack.append(i)

            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            
        return True if not stack else False


