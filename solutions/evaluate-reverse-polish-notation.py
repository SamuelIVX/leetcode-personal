 # Problem: Evaluate Reverse Polish Notation
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
 # Tags: Array, Math, Stack

class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                elif t == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(float(a) / b))
        return stack[-1]

                
