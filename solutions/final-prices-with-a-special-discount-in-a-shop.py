 # Problem: Final Prices With a Special Discount in a Shop
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
 # Tags: Array, Stack, Monotonic Stack

class Solution(object):
    def finalPrices(self, prices):
        res = [p for p in prices]
        stack = []

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                res[j] -= prices[i]
            stack.append(i)
        return res
