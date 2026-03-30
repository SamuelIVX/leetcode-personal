 # Problem: Best Time to Buy and Sell Stock
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
 # Tags: Array, Dynamic Programming

class Solution(object):
    def maxProfit(self, prices):
        cheapest_price = prices[0]
        maximum_profit = 0

        for p in prices:
            cheapest_price = min(cheapest_price, p)
            maximum_profit = max(maximum_profit, p-cheapest_price)

        return maximum_profit
