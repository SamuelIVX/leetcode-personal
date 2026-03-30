 # Problem: Maximum Strong Pair XOR I
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/maximum-strong-pair-xor-i/
 # Tags: Array, Hash Table, Bit Manipulation, Trie, Sliding Window

class Solution(object):
    def maximumStrongPairXor(self, nums):
        maxx = 0

        nums.sort()

        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if abs(nums[x] - nums[y]) <= min(nums[x],nums[y]): maxx = max(maxx, nums[x] ^ nums[y])
        return maxx
