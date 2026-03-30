 # Problem: Implement Queue using Stacks
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/implement-queue-using-stacks/
 # Tags: Stack, Design, Queue

class MyQueue(object):

    def __init__(self):
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack.pop(0)

    def peek(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[0]

    def empty(self):
        """
        :rtype: bool
        """
        return False if self.stack else True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
