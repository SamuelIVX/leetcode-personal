 # Problem: Defuse the Bomb
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/defuse-the-bomb/
 # Tags: Array, Sliding Window

class Solution(object):
    def decrypt(self, code, k):
        n = len(code)
        res = [0] * n

        left = 0
        curr_sum = 0

        for r in range(n + abs(k)):
            curr_sum += code[r % n]

            if r - left + 1 > abs(k):
                curr_sum -= code[left % n]
                left = (left + 1) % n

            if r - left + 1 == abs(k):
                if k > 0:
                    res[(left - 1) % n] = curr_sum
                elif k < 0:
                    res[(r + 1) % n] = curr_sum
        return res
                
