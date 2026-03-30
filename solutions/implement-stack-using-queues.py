 # Problem: Implement Stack using Queues
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/implement-stack-using-queues/
 # Tags: Stack, Design, Queue

from collections import deque
class MyStack(object):

    def __init__(self):
        self.q = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.q:
            return self.q.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.q:
            return self.q[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return False if self.q else True
        
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
