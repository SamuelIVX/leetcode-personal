 # Problem: Maximum Product Difference Between Two Pairs
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
 # Tags: Array, Sorting

class Solution(object):
    def maxProductDifference(self, nums):
        highest = (float('-inf')) 
        lowest = (float('inf')) 
        second_highest = second_lowest = 0

        for n in nums:
            if n > highest:
                second_highest = highest
                highest = n
            elif n > second_highest:
                second_highest = n
            
            if n < lowest:
                second_lowest = lowest
                lowest = n
            elif n < second_lowest:
                second_lowest = n

        return (highest * second_highest) - (lowest * second_lowest)
