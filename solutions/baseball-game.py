 # Problem: Baseball Game
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/baseball-game/
 # Tags: Array, Stack, Simulation

class Solution(object):
    def calPoints(self, operations):
        stack = deque()
        total_sum = 0
        for i in operations:
            if i == "+":
                previous = int(stack[-1]) if len(stack) >= 1 else 0
                second_previous = int(stack[-2]) if len(stack) >= 2 else 0
                stack.append(previous + second_previous)
                total_sum += previous + second_previous
            elif i == "D":
                previous = int(stack[-1]) if len(stack) >= 1 else 0
                stack.append(previous * 2)
                total_sum += previous * 2
            elif i == "C":
                total_sum -= int(stack.pop())
            else:
                stack.append(i)
                total_sum += int(i)
        return total_sum
        # stack = []
        # for i in operations:
        #     if i == '+':
        #         stack.append(stack[-1] + stack[-2])
        #     elif i == 'C':
        #         stack.pop()
        #     elif i == 'D':
        #         stack.append(2 * stack[-1])
        #     else:
        #         stack.append(int(i))
        # return sum(stack)

