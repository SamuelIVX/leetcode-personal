 # Problem: Number of Good Pairs
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/number-of-good-pairs/
 # Tags: Array, Hash Table, Math, Counting

class Solution(object):
    def numIdenticalPairs(self, nums):
        counter = defaultdict(int)
        pairs = 0
        for i in nums:
            counter[i] += 1
        
        for value in counter.values():
            if value > 1:
                expected_sum = value*(value - 1) // 2
                pairs += expected_sum
        return pairs
