 # Problem: Minimum Size Subarray Sum
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/minimum-size-subarray-sum/
 # Tags: Array, Binary Search, Sliding Window, Prefix Sum

class Solution(object):
    def minSubArrayLen(self, target, nums):
        left, total = 0,0
        res = float('inf')

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                res = min(res, right - left + 1 )
                total -= nums[left]
                left += 1
        return 0 if res == float('inf') else res
