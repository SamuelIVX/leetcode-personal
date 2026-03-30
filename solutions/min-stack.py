 # Problem: Min Stack
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/min-stack/
 # Tags: Stack, Design

from collections import deque
class MinStack(object):

    def __init__(self):
        self.q = deque()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.q.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if self.q:
            return self.q.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.q:
            return self.q[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.q:
            return min(self.q)
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
