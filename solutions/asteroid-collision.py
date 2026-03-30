 # Problem: Asteroid Collision
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/asteroid-collision/
 # Tags: Array, Stack, Simulation

class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []

        for a in asteroids:
            if a > 0:
                stack.append(a)
            elif a < 0:
                while stack and stack[-1] > 0 and abs(a) > stack[-1]:
                    stack.pop()

                if not stack or stack[-1] < 0:
                    stack.append(a)
                elif stack and stack[-1] == abs(a):
                    stack.pop()
                    continue
        return stack
