 # Problem: Maximum Average Subarray I
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/maximum-average-subarray-i/
 # Tags: Array, Sliding Window

class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)
        window_sum = sum(nums[:k])
        maxx = float(window_sum)

        for i in range(n - k):
            window_sum = (window_sum - nums[i]) + nums[i + k]
            if window_sum > maxx: maxx = window_sum

        return float(maxx)/k

