 # Problem: Build an Array With Stack Operations
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/build-an-array-with-stack-operations/
 # Tags: Array, Stack, Simulation

class Solution(object):
    def buildArray(self, target, n):
        res = []
        stack = []
        
        for i in range(1, n+1):
            stack.append(i)
            res.append("Push")

            if stack and i not in target:
                stack.pop()
                res.append("Pop")

            if stack == target:
                break
        
        return res
